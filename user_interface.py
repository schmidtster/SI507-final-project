from secrets import plotly_key, plotly_username
from lib_blog import *
import sqlite3 as sqlite
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import operator
plotly.tools.set_credentials_file(username=plotly_username, api_key=plotly_key)


db_name = "blogs.db"


def process_tags(orderby="count", desc="desc", limit=None):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    base_statement = "SELECT Tags.TagName, Tags.NumberUsed, Tags.Id FROM Tags"
    tag_names = []
    tag_count = []

    if orderby == "alpha":
        statement = " ORDER BY Tags.TagName"
        base_statement += statement
        if desc == "asc":
            statement = " asc"
            base_statement += statement
            if limit is not None:
                statement = " LIMIT {}".format(int(limit))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
        else:
            base_statement += " desc"
            if limit is not None:
                statement = " LIMIT {}".format(int(limit))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
    else:
        statement = " ORDER BY Tags.NumberUsed"
        base_statement += statement
        if desc == "asc":
            statement = " asc"
            base_statement += statement
            if limit is not None:
                statement = " LIMIT {}".format(int(limit))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
        else:
            base_statement += " desc"
            if limit is not None:
                statement = " LIMIT {}".format(int(limit))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    tag_names.append(result[0])
                    tag_count.append(result[1])
    tags_index = {}
    count = 1
    print("{:<5} | {:<30.25} | {:<5} \n".format("Index", "Tags", "Count"))
    for result in results:
        output = "{:<5} | {:<30.25} | {:<5}".format(count, result[0], result[1])
        print(output)
        sql = "SELECT Blogs.Title, Blogs.CompleteURL FROM Blogs JOIN TagAssociations ON Blogs.Id = " \
              "TagAssociations.BlogTitle WHERE TagAssociations.TagName = {}".format(result[2])
        result = cur.execute(sql)
        result_list = result.fetchall()
        tags_index[count] = result_list
        count += 1
    conn.close()
    return tag_count, tag_names, tags_index


def tags_bar_graph(tag_count, tag_names):
    data = [go.Bar(
        x=tag_names,
        y=tag_count,
        text=tag_count,
        textposition='auto',
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )]
    py.plot(data, filename="tags_bar_graph", auto_open=True)
    return "Opening a new tab in your web browser..."


def process_authors(orderby="count", desc="desc", limit_authors=None):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    base_statement = "SELECT Authors.FullName, Authors.NumberBlogs, Authors.URL, Authors.Id FROM Authors"
    authors = []
    values = []
    urls = []

    if orderby == "alpha":
        statement = " ORDER BY Authors.LastName"
        base_statement += statement
        if desc == "asc":
            statement = " asc"
            base_statement += statement
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
        else:
            base_statement += " desc"
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
    else:
        statement = " ORDER BY Authors.NumberBlogs"
        base_statement += statement
        if desc == "asc":
            statement = " asc"
            base_statement += statement
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
        else:
            base_statement += " desc"
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
                    urls.append(result[2])
    authors_index = {}
    count = 1
    print("{:<5} | {:<30.25} | {:<3} | {:<50} \n".format("Index", "Author", "Count", "URL"))
    for result in results:
        output = "{:<5} | {:<30.25} | {:<3} | {:<50}".format(count, result[0], result[1], result[2])
        print(output)
        sql = "SELECT Authors.FullName, Blogs.Title, Blogs.Description, Blogs.Date, Blogs.CompleteURL FROM Blogs " \
              "JOIN Authors ON Blogs.AuthorId = Authors.Id WHERE Blogs.AuthorId = {}".format(result[3])
        result = cur.execute(sql)
        result_list = result.fetchall()
        authors_index[count] = result_list
        count += 1
    conn.close()
    return authors, values, urls, authors_index


def authors_pie_chart(authors, values):
    trace = go.Pie(labels=authors, values=values)
    py.plot([trace], filename="Blogs Per Author", auto_open=True)
    return "Opening a new tab in your web browser..."


def process_comments(limit=None):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    dates = []
    total_comments_per_month = []

    if limit is not None:
        statement = "SELECT Blogs.Date, Blogs.Comments FROM Blogs ORDER BY Blogs.Id asc"
        execute = cur.execute(statement)
        results = execute.fetchall()
        running_total = 0
        list_index = -1
        for result in results:
            split_result = result[0].split()
            month_year = split_result[0] + " " + split_result[2]
            if month_year not in dates:
                dates.append(month_year)
                total_comments_per_month.append(running_total)
                list_index += 1
                running_total = int(result[1])
            else:
                running_total += int(result[1])
                total_comments_per_month[list_index] = running_total
            if len(dates) > int(limit):
                del dates[-1]
                del total_comments_per_month[-1]
                break
        dates_index = {}
        count = 1
        print("{:<5} | {:<17.17} | {:<5} \n".format("Index", "Month, Year", "Total Comments"))
        for row in range(len(dates)):
            output = "{:<5} | {:<17.17} | {:<5}".format(count, dates[row], total_comments_per_month[row])
            print(output)
            month_year_split = dates[row].split()
            sql = "SELECT Blogs.Title, Authors.FullName, Blogs.Date, Blogs.Comments, Blogs.CompleteURL FROM Blogs " \
                  "JOIN Authors ON Blogs.AuthorId = Authors.Id WHERE Blogs.Date " \
                  "LIKE '%{}% %{}%'".format(month_year_split[0], month_year_split[1])
            result = cur.execute(sql)
            result_list = result.fetchall()
            dates_index[count] = result_list
            count += 1
        conn.close()
        return dates, total_comments_per_month, dates_index
    else:
        statement = "SELECT Blogs.Date, Blogs.Comments FROM Blogs ORDER BY Blogs.Id desc"
        execute = cur.execute(statement)
        results = execute.fetchall()
        running_total = 0
        list_index = -1
        for result in results:
            split_result = result[0].split()
            month_year = split_result[0] + " " + split_result[2]
            if month_year not in dates:
                dates.append(month_year)
                total_comments_per_month.append(running_total)
                list_index += 1
                running_total = int(result[1])
            else:
                running_total += int(result[1])
                total_comments_per_month[list_index] = running_total
        dates_index = {}
        count = 1
        print("{:<5} | {:<17.17} | {:<5} \n".format("Index", "Month, Year", "Total Comments"))
        for row in range(len(dates)):
            output = "{:<5} | {:<17.17} | {:<5}".format(count, dates[row], total_comments_per_month[row])
            print(output)
            month_year_split = dates[row].split()
            sql = "SELECT Blogs.Title, Authors.FullName, Blogs.Date, Blogs.Comments, Blogs.CompleteURL FROM Blogs " \
                  "JOIN Authors ON Blogs.AuthorId = Authors.Id WHERE Blogs.Date LIKE" \
                  " '%{}% %{}%'".format(month_year_split[0], month_year_split[1])
            result = cur.execute(sql)
            result_list = result.fetchall()
            dates_index[count] = result_list
            count += 1
        conn.close()
        return dates, total_comments_per_month, dates_index


def comments_line_graph(dates, comments):
    trace0 = go.Scatter(
        x=dates,
        y=comments,
        mode='lines',
        name='lines'
    )
    data = [trace0]

    py.plot(data, filename='Comments Per Month', auto_open=True)
    return "Opening a new tab in your web browser..."


def process_images():
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    blogsites = []
    img_counts = []
    returnblogsites = {}

    statement = "SELECT BlogSites.Name, Blogs.Images FROM Blogs JOIN BlogSites WHERE Blogs.BlogSite = BlogSites.Id"
    execution = cur.execute(statement)
    results = execution.fetchall()
    for result in results:
        blogsites.append(result[0])
        if result[0] not in returnblogsites:
            returnblogsites[result[0]] = result[1]
        else:
            returnblogsites[result[0]] += result[1]
        img_counts.append(result[1])

    sorted_blogs = sorted(returnblogsites.items(), reverse=True, key=operator.itemgetter(1))
    print("{:<30.25} | {:<5} \n".format("Blog Site Name", "Count of Images for all Blogs"))
    for result in sorted_blogs:
        print("{:<30.25} | {:<5}".format(result[0], result[1]))
    conn.close()
    return sorted_blogs, blogsites, img_counts


def images_histogram(blogsites, img_counts):
    data = [
        go.Histogram(
            histfunc="sum",
            y=img_counts,
            x=blogsites,
            name="Total Images per Blog Site"
        ),
        go.Histogram(
            histfunc="avg",
            y=img_counts,
            x=blogsites,
            name="Average Images per Blog Post"
        )
    ]

    py.plot(data, filename='Images Per Blogsite and Sum', auto_open=True)
    return "Opening a new tab in your web browser..."


def most_recent(limit=10):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    count = 1
    if limit is not 10:
        statement = "SELECT Blogs.Title, Authors.FullName, Blogs.Date, Blogs.Description, Blogsites.Name, " \
                    "Blogs.CompleteURL " \
                    "FROM Blogs JOIN Authors ON Blogs.AuthorId = Authors.Id JOIN BlogSites ON Blogs.BlogSite = " \
                    "BlogSites.Id LIMIT {}".format(limit)
        execute = cur.execute(statement)
        results = execute.fetchall()
        print("{:<5} | {:<30.28} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format("Index",
                                                                                                  "Title",
                                                                                                  "Author",
                                                                                                  "Date Published",
                                                                                                  "Description",
                                                                                                  "Blog Site",
                                                                                                  "Complete URL \n"))
        for each_result in results:
            print("{:<5} | {:<30.28} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format(count,
                                                                                                      each_result[0],
                                                                                                      each_result[1],
                                                                                                      each_result[2],
                                                                                                      each_result[3],
                                                                                                      each_result[4],
                                                                                                      each_result[5]))
            count += 1
    else:
        statement = "SELECT Blogs.Title, Authors.FullName, Blogs.Date, Blogs.Description, Blogsites.Name, " \
                    "Blogs.CompleteURL " \
                    "FROM Blogs JOIN Authors ON Blogs.AuthorId = Authors.Id JOIN BlogSites ON Blogs.BlogSite = " \
                    "BlogSites.Id LIMIT 10"
        execute = cur.execute(statement)
        results = execute.fetchall()
        print("{:<5} | {:<30.28} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format("Index", "Title",
                                                                                                  "Author",
                                                                                                  "Date Published",
                                                                                                  "Description",
                                                                                                  "Blog Site",
                                                                                                  "Complete URL \n"))
        for each_result in results:
            print("{:<5} | {:<30.28} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format(count,
                                                                                                      each_result[0],
                                                                                                      each_result[1],
                                                                                                      each_result[2],
                                                                                                      each_result[3],
                                                                                                      each_result[4],
                                                                                                      each_result[5]))
            count += 1
    return results


# USER INTERFACE
def load_help_text():
    with open('helpfp.txt') as f:
        return f.read()


def user_interface():
    try:
        open("BLOG_CACHE.json", "r").close()
        conn = sqlite.connect(db_name)
        cur = cur = conn.cursor()
        sql_text = "SELECT Name FROM Blogsites"
        result = cur.execute(sql_text)
        conn.close()
    except Exception as error8:
        print("No database or cache file found. Creating cache and database...", error8)
        clean = clean_database()
        print(clean)
        data_entry = enter_data_to_db()
        print(data_entry)
        update_comp = update_records()
        print(update_comp)
    help_text = load_help_text()
    tags_commands = ["tags", "count", "alpha", "desc", "asc", "limit", "graph"]
    authors_commands = ["authors", "count", "alpha", "desc", "asc", "limit", "graph"]
    comments_commands = ["comments", "limit", "graph"]
    images_commands = ["images", "graph"]
    most_recent_commands = ["most_recent", "limit"]
    response = ""
    while response != "exit":
        response = input('Enter a command: ')
        response_list = response.split()
        if tags_commands[0] in response_list:
            command_list = ["count", "desc", None, ""]
            for each_parameter in response_list:
                if "=" in each_parameter:
                    params = each_parameter.split("=")
                    if params[0] == tags_commands[5]:
                        command_list[2] = params[1]
                elif each_parameter in tags_commands[1:3]:
                    command_list[0] = each_parameter
                elif each_parameter in tags_commands[3:5]:
                    command_list[1] = each_parameter
                elif each_parameter == tags_commands[6]:
                    command_list[3] = each_parameter
                elif each_parameter == tags_commands[0]:
                    pass
                else:
                    print("Command not recognized: ", response)
                    user_interface()
            command_processed = process_tags(command_list[0], command_list[1], command_list[2])
            if command_list[3] != "":
                make_graph = tags_bar_graph(command_processed[0], command_processed[1])
                print(make_graph)

            tags_input = ""
            while tags_input != "no":
                tags_input = input(
                    "Would you like to view the articles associated with a tag? Type the number or type 'no' to return "
                    "to main display: ")
                if tags_input == "no":
                    break
                else:
                    try:
                        int(tags_input)
                        print("{:<5} | {:<40.35} | {:<20}".format("Index", "Blog Title", "Blog URL"))
                        if int(tags_input) in command_processed[2].keys():
                            count = 1
                            for each_value in command_processed[2][int(tags_input)]:
                                output = "{:<5} | {:<40.38} | {:<20}".format(count, each_value[0], each_value[1])
                                count += 1
                                print(output)
                        else:
                            print("Index not found, please try again.")
                    except Exception as error6:
                        print("Please type in a number.", error6)

        elif authors_commands[0] in response_list:
            command_list = ["count", "desc", None, ""]
            for each_parameter in response_list:
                if "=" in each_parameter:
                    params = each_parameter.split("=")
                    if params[0] == authors_commands[5]:
                        command_list[2] = params[1]
                elif each_parameter in authors_commands[1:3]:
                    command_list[0] = each_parameter
                elif each_parameter in authors_commands[3:5]:
                    command_list[1] = each_parameter
                elif each_parameter == authors_commands[6]:
                    command_list[3] = each_parameter
                elif each_parameter == authors_commands[0]:
                    pass
                else:
                    print("Command not recognized: ", response)
                    user_interface()
            command_processed = process_authors(command_list[0], command_list[1], command_list[2])
            if command_list[3] != "":
                make_graph = authors_pie_chart(command_processed[0], command_processed[1])
                print(make_graph)

            authors_input = ""
            while authors_input != "no":
                authors_input = input(
                    "Would you like to view the articles associated with an author? Type the number or type 'no' to "
                    "return to main display: ")
                if authors_input == "no":
                    break
                else:
                    print("{:<5} | {:<30.30} | {:<40.40} | {:<20.20} | {:<50}".format("Index",
                                                                                      "Title",
                                                                                      "Description",
                                                                                      "Date",
                                                                                      "Blog URL"))
                    try:
                        int(authors_input)
                        if int(authors_input) in command_processed[3].keys():
                            count = 1
                            for each_value in command_processed[3][int(authors_input)]:
                                output = "{:<5} | {:<30.30} | {:<40.40} | {:<20.20} | {:<50}".format(count,
                                                                                                     each_value[1],
                                                                                                     each_value[2],
                                                                                                     each_value[3],
                                                                                                     each_value[4])
                                count += 1
                                print(output)
                        else:
                            print("Index not found, please try again.")
                    except Exception as error7:
                        print("Please type in a number.", error7)

        elif comments_commands[0] in response_list:
            command_list = ["", ""]
            for each_parameter in response_list:
                if "=" in each_parameter:
                    params = each_parameter.split("=")
                    if params[0] == comments_commands[1]:
                        command_list[0] = params[1]
                elif each_parameter == comments_commands[2]:
                    command_list[1] = each_parameter
                elif each_parameter == comments_commands[0]:
                    pass
                else:
                    print("Command not recognized: ", response)
                    user_interface()
            if command_list[0] != "":
                command_processed = process_comments(command_list[0])
            else:
                command_processed = process_comments()
            if command_list[1] != "":
                make_graph = comments_line_graph(command_processed[0], command_processed[1])
                print(make_graph)

            comments_input = ""
            while comments_input != "no":
                comments_input = input(
                    "Would you like to view the articles associated with an author? Type the number or type 'no' to "
                    "return to main display: ")
                if comments_input == "no":
                    break
                else:
                    print("{:<5} | {:<40.38} | {:<25.25} | {:<17.17} | {:<8} | {:<50}".format("Index",
                                                                                              "Title",
                                                                                              "Author",
                                                                                              "Date",
                                                                                              "Comments",
                                                                                              "Blog URL"))
                    try:
                        int(comments_input)
                        if int(comments_input) in command_processed[2].keys():
                            count = 1
                            for each_value in command_processed[2][int(comments_input)]:
                                output = "{:<5} | {:<40.38} | {:<25.25} | {:<17.17} | {:<8} | {:<50}"\
                                    .format(count, each_value[0], each_value[1], each_value[2], each_value[3],
                                            each_value[4])
                                count += 1
                                print(output)
                        else:
                            print("Index not found, please try again.")
                    except Exception as error7:
                        print("Please type in a number.", error7)

        elif images_commands[0] in response_list:
            command_list = [""]
            if len(response_list) == 2:
                for each_parameter in response_list:
                    if each_parameter == images_commands[0]:
                        pass
                    elif each_parameter == images_commands[1]:
                        command_list[0] = each_parameter
                    else:
                        print("Command not recognized: ", response)
                        user_interface()
            command_processed = process_images()
            if command_list[0] != "":
                make_graph = images_histogram(command_processed[1], command_processed[2])
                print(make_graph)

        elif most_recent_commands[0] in response_list:
            if len(response_list) == 2:
                for each_parameter in response_list:
                    if "=" in each_parameter:
                        params = each_parameter.split("=")
                        if params[0] == most_recent_commands[1]:
                            try:
                                convert_str = int(params[1])
                                most_recent(convert_str)
                            except Exception as error:
                                print("A valid integer is needed. Please type a valid integer after 'limit='", error)
                                user_interface()
                    elif most_recent_commands[0] == each_parameter:
                        pass
                    else:
                        print("Command not recognized: ", response)
                        user_interface()
            elif len(response_list) == 1:
                most_recent()
            else:
                print("Command not recognized: ", response)
                user_interface()

        elif "wipe" in response_list:
            if "refresh" in response_list:
                clean = clean_database()
                print(clean)
                data_entry = enter_data_to_db(staleness=0)
                print(data_entry)
                update_comp = update_records()
                print(update_comp)
            else:
                clean = clean_database()
                print(clean)
                data_entry = enter_data_to_db()
                print(data_entry)
                update_comp = update_records()
                print(update_comp)
            continue

        elif response == "help":
            print(help_text)
            continue

        elif response == "exit":
            response = response
            print("Exiting the program...")

        else:
            print("Command not recognized: ", response)
            user_interface()


user_interface()
