import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3 as sqlite
import json


class BlogPost:
    def __init__(self, title, authorfull, authorfirst, authorlast, authorurl, date, description, blogsite, url):
        self.title = title
        self.authorfull = authorfull
        self.authorfirst = authorfirst
        self.authorlast = authorlast
        self.authorurl = authorurl
        self.date = date
        self.description = description
        self.blogsite = blogsite
        self.url = url
        self.tags = []
        self.comments = 0
        self.images = 0
        self.blogdesciption = ""
        self.complete_url = ""

        # tags, comments, images
        blog_base_url = "https://www.lib.umich.edu"
        self.complete_url = blog_base_url + self.url
        header = {"User-Agent": "SI_CLASS"}
        page_text = make_request_using_cache(blog_url=self.complete_url, header=header)
        site_soup = BeautifulSoup(page_text, "html.parser")

        main_content = site_soup.find(id="main-content")
        pane_content = main_content.find(class_="pane-content")

        image_per_post = pane_content.find_all("img")
        self.images = len(image_per_post)

        try:
            tag_section = pane_content.find(class_="item-list")
            tag_list = tag_section.find_all("li")
            for each_tag in tag_list:
                if "'" in each_tag.string.strip():
                    replacement = each_tag.string.strip().replace("'", "")
                    self.tags.append(replacement)
                else:
                    self.tags.append(each_tag.string.strip())
        except Exception as error:
            error

        try:
            comment_section = pane_content.find(class_="comments")
            comment_count = comment_section.find("h3").text
            split_comment_count = comment_count.split()
            count = int(split_comment_count[0])
            self.comments = count
            print("Comments found: ", count)
        except Exception as error:
            error

        banner_section = site_soup.find(id="block-mlibrary-blog-banner")
        blog_description = banner_section.find("p").string.strip()
        if "'" in blog_description:
            replacement = blog_description.replace("'", "`")  # does not replace all apostrophes, will have to do regex
            self.blogdesciption = replacement
        else:
            self.blogdesciption = blog_description

    def to_json(self):
        return {"Title": self.title,
                "AuthorFull": self.authorfull,
                "AuthorFirst": self.authorfirst,
                "AuthorLast": self.authorlast,
                "AuthorURL": self.authorurl,
                "Date": self.date,
                "Description": self.description,
                "BlogSite": self.blogsite,
                "URL": self.url,
                "CompleteURL": self.complete_url,
                "Tags": self.tags,
                "Comments": self.comments,
                "Images": self.images,
                "BlogDescription": self.blogdesciption}

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.title, self.authorfull, self.date, self.description,
                                                   self.blogsite, self.url, self.tags, self.comments, self.images)


try:
    open_cache = open("BLOG_CACHE.json", "r")
    read_cache = open_cache.read()
    BLOG_CACHE = json.loads(read_cache)
    open_cache.close()
except Exception as e:
    BLOG_CACHE = {}
    print(e)

MAX_STALENESS = 200000


def is_fresh(cache_entry):
    now = datetime.now().timestamp()
    staleness = now - cache_entry['cache_timestamp']
    return staleness < MAX_STALENESS


def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


def get_unique_key(url):
    return url


def make_request_using_cache(blog_url="", header=""):
    unique_ident = get_unique_key(blog_url)
    if unique_ident in BLOG_CACHE:
        if is_fresh(BLOG_CACHE[unique_ident]):
            print("Getting cached data...")
            return BLOG_CACHE[unique_ident]["content"]
        else:
            print("Making a request for new data...")
            page_text = requests.get(blog_url, headers=header).text
            BLOG_CACHE[unique_ident] = {"content": page_text}
            BLOG_CACHE[unique_ident]['cache_timestamp'] = datetime.now().timestamp()
            fw = open("BLOG_CACHE.json", "w")
            dumped_json_cache = json.dumps(BLOG_CACHE)
            fw.write(dumped_json_cache)
            fw.close()
            return BLOG_CACHE[unique_ident]["content"]
    else:
        print("Making a request for new data...")
        page_text = requests.get(blog_url, headers=header).text
        BLOG_CACHE[unique_ident] = {"content": page_text}
        BLOG_CACHE[unique_ident]['cache_timestamp'] = datetime.now().timestamp()
        fw = open("BLOG_CACHE.json", "w")
        dumped_json_cache = json.dumps(BLOG_CACHE)
        fw.write(dumped_json_cache)
        fw.close()
        return BLOG_CACHE[unique_ident]["content"]


def get_blogs():
    class_instances = []
    page_count = 0
    blog_base_url = "https://www.lib.umich.edu"
    page_string = "/blogs?page={}".format(page_count)
    while True:
        header = {"User-Agent": "SI_CLASS"}
        full_url = blog_base_url + page_string
        print(full_url)
        blog_text = make_request_using_cache(full_url, header)
        site_soup = BeautifulSoup(blog_text, "html.parser")

        main_content = site_soup.find(id="main-content")
        view_content = main_content.find_all(class_="view-content")
        blogsites = []
        urls = []
        titles = []
        descriptions = []
        dates = []
        authorsfull = []
        authorsfirst = []
        authorslast = []
        authorurls = []

        for results in view_content:
            headers = results.find_all(class_="blog-banner")
            for header in headers:
                if not isinstance(header, str):
                    blogsite = header.find(class_="content")
                    if "'" in blogsite.string.strip():
                        replacement = blogsite.string.strip().replace("'", "")
                        blogsites.append(replacement)
                    else:
                        blogsites.append(blogsite.string.strip())
            titles_results = results.find_all("h3")
            for title in titles_results:
                if not isinstance(title, str):
                    href = title.find("a")["href"]
                    urls.append(href)
                    title_main = title.find("a")
                    if "'" in title_main.string:
                        replacement = title_main.string.replace("'", "")
                        titles.append(replacement)
                    else:
                        titles.append(title_main.string)
            description_art = results.find_all(class_="article-body")
            for description in description_art:
                if not isinstance(description, str):
                    desc = description.string.strip()
                    descriptions.append(desc)
            footers = results.find_all(class_="byline")
            for footer in footers:
                if not isinstance(footer, str):
                    date = footer.text.split("\n")
                    dates.append(date[1].strip())
                    author = footer.find("a").text.replace("See all posts by ", "")
                    if author == " ":
                        authorsfull.append("No author")
                        authorsfirst.append("No author")
                        authorslast.append("No author")
                        authorurls.append("No URL")
                    else:
                        if "'" in author:
                            replacement = author.replace("'", "")
                            authorsfull.append(replacement)
                            author_split = replacement.split()
                            first_name = ""
                            for name in author_split[:-1]:
                                first_name += name + " "
                            authorsfirst.append(first_name.strip())
                            authorslast.append(author_split[-1])
                        else:
                            authorsfull.append(author)
                            author_split = author.split()
                            first_name = ""
                            for name in author_split[:-1]:
                                first_name += name + " "
                            authorsfirst.append(first_name.strip())
                            authorslast.append(author_split[-1])
                        authorurl = footer.find("a")["href"]
                        authorurls.append(authorurl)
        length = len(blogsites)
        if all(len(lst) == length for lst in [blogsites, urls, titles, descriptions, dates, authorsfull, authorsfirst,
                                              authorslast, authorurls]):
            count = 0
            for blogs in blogsites:
                individual_blog = BlogPost(titles[count], authorsfull[count], authorsfirst[count], authorslast[count],
                                           authorurls[count], dates[count], descriptions[count], blogsites[count],
                                           urls[count])
                count += 1
                class_instances.append(individual_blog)
        else:
            print("Error sequencing data...")
        try:
            check_older = main_content.find(class_="pager-next last")
            older_href = check_older.find("a")["href"]
            page_string = older_href
        except:
            break
    return class_instances


# instance_list = get_blogs()
# print(len(instance_list))

# Build DB Database
db_name = "blogs.db"


def clean_database():
    conn = sqlite.connect(db_name)
    cur = conn.cursor()

    statement = "DROP TABLE IF EXISTS 'Blogs'"
    cur.execute(statement)

    statement = "DROP TABLE IF EXISTS 'Authors'"
    cur.execute(statement)

    statement = "DROP TABLE IF EXISTS 'Tags'"
    cur.execute(statement)

    statement = "DROP TABLE IF EXISTS 'BlogSites'"
    cur.execute(statement)

    statement = "DROP TABLE IF EXISTS 'TagAssociations'"
    cur.execute(statement)

    statement = "CREATE TABLE 'Blogs' (" \
                "'Id' INTEGER PRIMARY KEY AUTOINCREMENT," \
                "'Title' TEXT," \
                "'AuthorId' INT," \
                "'AuthorFirstName' TEXT," \
                "'AuthorLastName' TEXT," \
                "'Date' TEXT," \
                "'Description' TEXT," \
                "'Comments' INT," \
                "'Images' INT," \
                "'BlogSite' TEXT," \
                "'CompleteURL' TEXT);"
    cur.execute(statement)

    statement = "CREATE TABLE 'Authors' (" \
                "'Id' INTEGER PRIMARY KEY AUTOINCREMENT," \
                "'FullName' TEXT," \
                "'FirstName' TEXT," \
                "'LastName' TEXT," \
                "'URL' TEXT," \
                "'NumberBlogs' INT);"
    cur.execute(statement)

    statement = "CREATE TABLE 'Tags' (" \
                "'Id' INTEGER PRIMARY KEY AUTOINCREMENT," \
                "'TagName' TEXT," \
                "'NumberUsed' INT);"
    cur.execute(statement)

    statement = "CREATE TABLE 'BlogSites' (" \
                "'Id' INTEGER PRIMARY KEY AUTOINCREMENT," \
                "'Name' TEXT," \
                "'Description' TEXT," \
                "'NumberBlogs' INT);"
    cur.execute(statement)

    statement = "CREATE TABLE 'TagAssociations' (" \
                "'Id' INTEGER PRIMARY KEY AUTOINCREMENT," \
                "'TagName' TEXT," \
                "'BlogTitle' TEXT);"
    cur.execute(statement)
    conn.close()
    return "Database wiped"


def enter_data_to_db(staleness=None):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    global MAX_STALENESS
    if staleness is not None:
        MAX_STALENESS = 0
    blogs = get_blogs()
    for blog in blogs:
        json_data = blog.to_json()
        insertion_json = (json_data["Title"], json_data["AuthorFirst"], json_data["AuthorLast"], json_data["Date"],
                          json_data["Description"],
                          json_data["Comments"], json_data["Images"], json_data["BlogSite"], json_data["CompleteURL"])
        statement_json = "INSERT INTO 'Blogs' (Title, AuthorFirstName, AuthorLastName, Date, Description, Comments, " \
                         "Images, BlogSite, " \
                         "CompleteURL)"
        statement_json += " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(statement_json, insertion_json)

        for each_tag in json_data["Tags"]:
            statement_json = "INSERT INTO 'Tags' (TagName)"
            statement_json += " VALUES (?)"
            cur.execute(statement_json, (each_tag,))

            insertion_json = (each_tag, json_data["Title"])
            statement_json = "INSERT INTO 'TagAssociations' (TagName, BlogTitle)"
            statement_json += " VALUES (?, ?)"
            cur.execute(statement_json, insertion_json)

        insertion_json = (json_data["AuthorFull"], json_data["AuthorFirst"], json_data["AuthorLast"],
                          json_data["AuthorURL"])
        statement_json = "INSERT INTO 'Authors' (FullName, FirstName, LastName, URL)"
        statement_json += "VALUES (?, ?, ?, ?)"
        cur.execute(statement_json, insertion_json)

        insertion_json = (json_data["BlogSite"], json_data["BlogDescription"])
        statement_json = "INSERT INTO 'BlogSites' (Name, Description)"
        statement_json += " VALUES (?, ?)"
        cur.execute(statement_json, insertion_json)
    conn.commit()
    conn.close()


def update_records():
    conn = sqlite.connect(db_name)
    cur = conn.cursor()

    statement = "DELETE FROM BlogSites WHERE Id NOT IN (SELECT MIN(Id) FROM BlogSites GROUP BY Name)"
    cur.execute(statement)

    statement = "DELETE FROM Tags WHERE Id NOT IN (SELECT MIN(Id) FROM Tags GROUP BY TagName)"
    cur.execute(statement)

    statement = "DELETE FROM Authors WHERE Id NOT IN (SELECT MIN(Id) FROM Authors GROUP BY FullName)"
    cur.execute(statement)

    statement = "SELECT Blogs.BlogSite, BlogSites.Id FROM Blogs JOIN BlogSites WHERE Blogs.BlogSite = BlogSites.Name"
    execute = cur.execute(statement)
    results = execute.fetchall()
    for each_result in results:
        statement = "UPDATE Blogs SET BlogSite = '{}' WHERE Blogs.BlogSite = '{}'".format(each_result[1],
                                                                                          each_result[0])
        cur.execute(statement)
        conn.commit()

    statement = "SELECT Blogs.AuthorFirstName, Blogs.AuthorLastName, Authors.Id FROM Blogs JOIN Authors WHERE " \
                "Blogs.AuthorFirstName = Authors.FirstName AND Blogs.AuthorLastName = Authors.LastName"
    execute = cur.execute(statement)
    results = execute.fetchall()
    for each_result in results:
        statement = "UPDATE Blogs SET AuthorId = '{}' WHERE Blogs.AuthorFirstName = '{}' AND Blogs.AuthorLastName = " \
                    "'{}'".format(each_result[2], each_result[0], each_result[1])
        cur.execute(statement)
        conn.commit()

    statement = "SELECT TagAssociations.TagName, Tags.Id FROM TagAssociations JOIN Tags WHERE " \
                "TagAssociations.TagName = Tags.TagName"
    execute = cur.execute(statement)
    results = execute.fetchall()
    for each_result in results:
        statement = "UPDATE TagAssociations SET TagName = '{}' WHERE TagAssociations.TagName = '{}'".format(
            each_result[1], each_result[0])
        cur.execute(statement)
        conn.commit()

    statement = "SELECT TagAssociations.BlogTitle, Blogs.Id FROM TagAssociations JOIN Blogs WHERE " \
                "TagAssociations.BlogTitle = Blogs.Title"
    execute = cur.execute(statement)
    results = execute.fetchall()
    for each_result in results:
        statement = "UPDATE TagAssociations SET BlogTitle = '{}' WHERE TagAssociations.BlogTitle = '{}'".format(
            each_result[1], each_result[0])
        cur.execute(statement)
        conn.commit()

    statement = "SELECT TagName, COUNT(BlogTitle) as cnt FROM TagAssociations GROUP BY TagName ORDER BY cnt DESC"
    execute = cur.execute(statement)
    results = execute.fetchall()
    for each_tag in results:
        statement = "UPDATE Tags SET NumberUsed = '{}' WHERE Tags.Id = '{}'".format(each_tag[1], each_tag[0])
        cur.execute(statement)
        conn.commit()

    statement = "SELECT AuthorId, COUNT(Title) as cnt FROM Blogs GROUP BY AuthorId ORDER BY cnt DESC"
    execute = cur.execute(statement)
    results = execute.fetchall()
    for each_author in results:
        statement = "UPDATE Authors SET NumberBlogs = '{}' WHERE Authors.Id = '{}'".format(each_author[1],
                                                                                           each_author[0])
        cur.execute(statement)
        conn.commit()

    statement = "SELECT BlogSite, COUNT(Title) as cnt FROM Blogs GROUP BY Blogsite ORDER BY cnt DESC"
    execute = cur.execute(statement)
    results = execute.fetchall()
    for each_author in results:
        statement = "UPDATE Blogsites SET NumberBlogs = '{}' WHERE BlogSites.Id = '{}'".format(each_author[1],
                                                                                               each_author[0])
        cur.execute(statement)
        conn.commit()
    return "Update successful"
