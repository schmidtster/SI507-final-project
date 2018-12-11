import unittest
from lib_blog import *
from user_interface import *


class TestScraping(unittest.TestCase):

    def blog_is_in_class_list(self, blog_title, blogsite, class_list):
        for blog in class_list:
            if blog_title == blog.title and blogsite == blog.blogsite:
                return True
        return False

    def test_class_instances(self):
        self.assertIsInstance(BlogPost("New Exhibit | Universal Declaration of Human Rights", "Kristine Greive",
                                       "Kristine", "Greive", "https://www.lib.umich.edu/blogs/kgreive",
                                       "December 7, 2018",
                                       "The Special Collections Research Center is pleased to announce a new exhibit "
                                       "celebrating the 60th anniversary of the Universal Declaration of Human Rights. "
                                       "Visit the Special Collections Exhibit Gallery in our 6th floor space "
                                       "(660J Hatcher South) to see the exhibit, Universal Declaration of Human Rights"
                                       ": Linocuts by Meredith Stern, on view now through February 1, 2019.",
                                       "Beyond the Reading Room",
                                       "/blogs/beyond-reading-room/new-exhibit-universal-declaration-human-rights"),
                              BlogPost)
        blog_instance = BlogPost("New Exhibit | Universal Declaration of Human Rights", "Kristine Greive", "Kristine",
                                 "Greive", "https://www.lib.umich.edu/blogs/kgreive", "December 7, 2018",
                                 "The Special Collections Research Center is pleased to announce a new exhibit "
                                 "celebrating the 60th anniversary of the Universal Declaration of Human Rights. Visit "
                                 "the Special Collections Exhibit Gallery in our 6th floor space (660J Hatcher South) "
                                 "to see the exhibit, Universal Declaration of Human Rights: Linocuts by Meredith "
                                 "Stern, on view now through February 1, 2019.", "Beyond the Reading Room",
                                 "/blogs/beyond-reading-room/new-exhibit-universal-declaration-human-rights")
        self.assertEqual(blog_instance.tags, ["exhibits"])
        self.assertEqual(blog_instance.complete_url, "https://www.lib.umich.edu/blogs/beyond-reading-room/new-exhibit-"
                                                     "universal-declaration-human-rights", "Beyond the Reading Room", )
        pass

    def test_scraping(self):
        self.assertGreaterEqual(len(get_blogs()), 693)
        list_of_class_instances = get_blogs()
        self.assertTrue(self.blog_is_in_class_list("New Exhibit | Universal Declaration of Human Rights",
                                                   "Beyond the Reading Room", list_of_class_instances))


class TestDatabase(unittest.TestCase):

    def test_tables_setup(self):
        conn = sqlite.connect(db_name)
        cur = conn.cursor()

        sql = 'SELECT FullName FROM Authors'
        results = cur.execute(sql)
        result_list = results.fetchall()
        for result in result_list:
            if "Kristine Greive" in result:
                self.assertIn('Kristine Greive', result)

        sql = '''
                            SELECT FullName, NumberBlogs
                            FROM Authors
                            WHERE NumberBlogs > 50
                            ORDER BY NumberBlogs DESC
                        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        # print(result_list)
        self.assertGreaterEqual(len(result_list), 3)
        self.assertGreaterEqual(result_list[0][1], 82)

        sql = 'SELECT Name FROM BlogSites'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('PIPEline',), result_list)
        self.assertEqual(len(result_list), 15)

        sql = '''
                                    SELECT Name, NumberBlogs
                                    FROM BlogSites
                                    WHERE NumberBlogs > 50
                                    ORDER BY NumberBlogs DESC
                                '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        # print(result_list)
        self.assertGreaterEqual(len(result_list), 5)

        sql = 'SELECT Title FROM Blogs'
        results = cur.execute(sql)
        result_list = results.fetchall()
        for result in result_list:
            if 'Asia Library Turns 70!' in result:
                self.assertIn('Asia Library Turns 70!', result)
        self.assertGreater(len(result_list), 690)

        sql = '''
                                    SELECT Title, Images
                                    FROM Blogs
                                    WHERE Images >= 10
                                    ORDER BY Images DESC
                                '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        # print(result_list)
        self.assertGreaterEqual(len(result_list), 10)

        sql = 'SELECT TagName FROM Tags'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('Digital Collections',), result_list)
        self.assertGreater(len(result_list), 300)

        sql = '''
                                    SELECT TagName, NumberUsed
                                    FROM Tags
                                    WHERE NumberUsed >= 10
                                    ORDER BY NumberUsed DESC
                                '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertGreaterEqual(len(result_list), 15)
        conn.close()

    def test_relations(self):
        conn = sqlite.connect(db_name)
        cur = conn.cursor()
        sql = "SELECT TagName, BlogTitle, Blogs.Title " \
              "FROM TagAssociations JOIN Blogs ON Blogs.Id = TagAssociations.BlogTitle " \
              "WHERE TagAssociations.BlogTitle = 99"
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertGreaterEqual(len(result_list), 0)

        sql = '''
                                    SELECT Blogs.AuthorId, Authors.Id, Authors.FullName
                                    FROM Blogs JOIN Authors ON Blogs.AuthorId = Authors.Id
                                '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        index = 0
        for result in result_list:
            if "Vicki J. Kondelik" in result:
                list_index = index
                self.assertIn('Vicki J Kondelik', result_list[list_index])
            else:
                index += 1

        sql = "SELECT Blogsite, Blogsites.Id, Blogsites.Name FROM Blogs JOIN BlogSites ON Blogs.BlogSite = Blogsites.Id"
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(int(result_list[0][0]), result_list[0][1])
        self.assertEqual(int(result_list[27][0]), result_list[27][1])

        conn.close()

    def test_random_rows(self):
        conn = sqlite.connect(db_name)
        cur = conn.cursor()
        sql = "SELECT Title, AuthorLastName, Date, Blogsite, CompleteURL FROM Blogs"
        results = cur.execute(sql)
        result_list = results.fetchall()
        index = 0
        for each_result in result_list:
            if "Asia Library Turns 70!" in each_result:
                list_index = index
                self.assertIn("Asia Library Turns 70!", result_list[list_index])
                self.assertIn("Lawson", result_list[list_index])
                self.assertIn("November 28, 2018", result_list[list_index])
                self.assertIn("https://www.lib.umich.edu/blogs/notes-asia-library/asia-library-turns-70-0",
                              result_list[list_index])
            else:
                index += 1

    def test_queries(self):
        conn = sqlite.connect(db_name)
        cur = conn.cursor()
        sql = "SELECT Blogs.Title, Authors.FullName, Blogs.Date, Blogs.Description, BlogSites.Name, " \
              "Blogs.CompleteURL FROM Blogs JOIN Authors ON Blogs.AuthorId = Authors.Id JOIN BlogSites " \
              "ON Blogs.BlogSite = BlogSites.Id LIMIT 4"
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn("December", result_list[0][2])


class TestUserInterface(unittest.TestCase):

    def test_tags_commands(self):
        data = process_tags(orderby="alpha", desc="asc", limit=10)
        self.assertEqual(data[1][0], "#LYD16")

        data = process_tags(limit=15)
        self.assertEqual(data[0][0], 73)
        self.assertEqual(data[1][14], "qualitative")

        try:
            data = process_tags(limit=30)
            tags_bar_graph(data[0], data[1])
        except Exception as error1:
            self.fail(msg=error1)

    def test_authors_commands(self):
        data = process_authors(orderby="alpha", desc="asc", limit_authors=15)
        self.assertEqual(data[2][0], "https://www.lib.umich.edu/blogs/rcadler")
        self.assertEqual(len(data[1]), 15)

        data = process_authors(orderby="count", desc="desc")
        self.assertGreaterEqual(len(data[1]), 140)
        self.assertEqual(data[0][1], "Vicki J Kondelik")

        try:
            auth_data = process_authors("asc", limit_authors=10)
            authors_pie_chart(auth_data[0], auth_data[1])
        except Exception as error2:
            self.fail(msg=error2)

    def test_comments_commands(self):
        data = process_comments(limit=12)
        self.assertEqual(data[1][11], 0)
        self.assertEqual(data[1][10], 5)
        self.assertEqual(len(data[0]), 12)

        try:
            results = process_comments()
            comments_line_graph(results[0], results[1])
        except Exception as error3:
            self.fail(msg=error3)

    def test_images_commands(self):
        data = process_images()
        self.assertEqual(len(data[0]), 15)
        self.assertEqual(data[0][0][0], "Beyond the Reading Room")

        try:
            results = process_images()
            images_histogram(results[1], results[2])
        except Exception as error4:
            self.fail(msg=error4)

    def test_most_recent_commands(self):
        data = most_recent()
        self.assertEqual(len(data), 10)
        list_of_recent_titles = []
        for blog in data:
            list_of_recent_titles.append(blog[0])
        self.assertIn("New Exhibit | Universal Declaration of Human Rights", list_of_recent_titles)


if __name__ == '__main__':
    unittest.main()
