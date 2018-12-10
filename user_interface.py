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
    base_statement = "SELECT Tags.TagName, Tags.NumberUsed FROM Tags"
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
    print("{:<30.25} | {:<5} \n".format("Tags", "Count"))
    for result in results:
        print("{:<30.25} | {:<5}".format(result[0], result[1]))
    conn.close()
    return tag_count, tag_names


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
    base_statement = "SELECT Authors.FullName, Authors.NumberBlogs, Authors.URL FROM Authors"
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
    print("{:<30.25} | {:<3} | {:<50.50} \n".format("Author", "Count", "URL"))
    for result in results:
        print("{:<30.25} | {:<3} | {:<50.50}".format(result[0], result[1], result[2]))
    conn.close()
    return authors, values, urls


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
        for result in results:
            split_result = result[0].split()
            month_year = split_result[0] + " " + split_result[2]
            if month_year not in dates:
                dates.append(month_year)
                total_comments_per_month.append(running_total)
                running_total = int(result[1])
            else:
                running_total += int(result[1])
            if len(dates) > int(limit):
                del dates[-1]
                del total_comments_per_month[-1]
                break
        print("{:<30.25} | {:<5} \n".format("Month, Year", "Total Comments"))
        for row in range(len(dates)):
            print("{:<30.25} | {:<5}".format(dates[row], total_comments_per_month[row]))
        conn.close()
        return dates, total_comments_per_month
    else:
        statement = "SELECT Blogs.Date, Blogs.Comments FROM Blogs ORDER BY Blogs.Id desc"
        execute = cur.execute(statement)
        results = execute.fetchall()
        running_total = 0
        for result in results:
            split_result = result[0].split()
            month_year = split_result[0] + " " + split_result[2]
            if month_year not in dates:
                dates.append(month_year)
                total_comments_per_month.append(running_total)
                running_total = int(result[1])
            else:
                running_total += int(result[1])
        print("{:<30.25} | {:<5} \n".format("Month, Year", "Total Comments"))
        for row in range(len(dates)):
            print("{:<30.25} | {:<5}".format(dates[row], total_comments_per_month[row]))
        conn.close()
        return dates, total_comments_per_month


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
    if limit is not 10:
        statement = "SELECT Blogs.Title, Authors.FullName, Blogs.Date, Blogs.Description, Blogsites.Name, " \
                    "Blogs.CompleteURL " \
                    "FROM Blogs JOIN Authors ON Blogs.AuthorId = Authors.Id JOIN BlogSites ON Blogs.BlogSite = " \
                    "BlogSites.Id LIMIT {}".format(limit)
        execute = cur.execute(statement)
        results = execute.fetchall()
        print("{:<30.25} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format("Title", "Author",
                                                                                          "Date Published",
                                                                                          "Description",
                                                                                          "Blog Site",
                                                                                          "Complete URL \n"))
        for each_result in results:
            print("{:<30.25} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format(each_result[0],
                                                                                              each_result[1],
                                                                                              each_result[2],
                                                                                              each_result[3],
                                                                                              each_result[4],
                                                                                              each_result[5]))
    else:
        statement = "SELECT Blogs.Title, Authors.FullName, Blogs.Date, Blogs.Description, Blogsites.Name, " \
                    "Blogs.CompleteURL " \
                    "FROM Blogs JOIN Authors ON Blogs.AuthorId = Authors.Id JOIN BlogSites ON Blogs.BlogSite = " \
                    "BlogSites.Id LIMIT 10"
        execute = cur.execute(statement)
        results = execute.fetchall()
        print("{:<30.25} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format("Title", "Author",
                                                                                          "Date Published",
                                                                                          "Description",
                                                                                          "Blog Site",
                                                                                          "Complete URL \n"))
        for each_result in results:
            print("{:<30.25} | {:<25.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format(each_result[0],
                                                                                              each_result[1],
                                                                                              each_result[2],
                                                                                              each_result[3],
                                                                                              each_result[4],
                                                                                              each_result[5]))
    return results


# def blogs_by_author(name="", limit=None):
#     conn = sqlite.connect(db_name)
#     cur = conn.cursor()
#     if limit is not None:
#         statement = "SELECT Blogs.Title, Blogs.Date, Blogs.Description, Blogsites.Name, Blogs.CompleteURL FROM Blogs
#         JOIN Blogsites ON Blogs.Blogsite = Blogsites.Id JOIN Authors on Blogs.AuthorId = Authors.Id WHERE
#         Authors.FullName LIKE '{}' LIMIT = {}".format(
#             name, limit)
#         execute = cur.execute(statement)
#         results = execute.fetchall()
#         print("{:<30.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format("Title", "Date Published",
#         "Description", "Blog Site Name", "CompleteURL \n"))
#         if results[0] != ():
#             for each_result in results:
#                 print("{:<30.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format(each_result[0],
#                                                                                    each_result[1],
#                                                                                    each_result[2],
#                                                                                    each_result[3],
#                                                                                    each_result[4]))
#         else:
#             print("No authors found by that name.")
#     else:
#         statement = "SELECT Blogs.Title, Blogs.Date, Blogs.Description, Blogsites.Name, Blogs.CompleteURL FROM
#         Blogs JOIN Blogsites ON Blogs.Blogsite = Blogsites.Id JOIN Authors on Blogs.AuthorId = Authors.Id WHERE
#         Authors.FullName LIKE '{}'".format(name)
#         execute = cur.execute(statement)
#         results = execute.fetchall()
#         print("{:<30.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format("Title", "Date Published",
#         "Description", "Blog Site Name", "CompleteURL \n"))
#         if results[0] != ():
#             for each_result in results:
#                 print("{:<30.25} | {:<20.20} | {:<40.35} | {:<25.25} | {:<40}".format(each_result[0],
#                                                                                    each_result[1],
#                                                                                    each_result[2],
#                                                                                    each_result[3],
#                                                                                    each_result[4]))
#         else:
#             print("No authors found by that name.")
#     return results


# USER INTERFACE


def load_help_text():
    with open('helpfp.txt') as f:
        return f.read()


def user_interface():
    help_text = load_help_text()
    tags_commands = ["tags", "count", "alpha", "desc", "asc", "limit", "graph"]
    authors_commands = ["authors", "count", "alpha", "desc", "asc", "limit", "graph"]
    comments_commands = ["comments", "limit", "graph"]
    images_commands = ["images", "graph"]
    most_recent_commands = ["most_recent", "limit"]
    # by_author_commands = ["blogs_by_author", "name", "limit"]
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

        # elif by_author_commands[0] in response_list:
        #     command_list = ["", ""]
        #     if len(response_list) >= 2:
        #         for each_parameter in response_list:
        #             if "=" in each_parameter:
        #                 params = each_parameter.split("=")
        #                 if by_author_commands[1] in params:
        #                     command_list[0] = each_parameter
        #                 elif by_author_commands[2] in params:
        #                     try:
        #                         convert_str = int(params[1])
        #                         command_list[1] = each_parameter
        #                     except Exception as e:
        #                         print("A valid integer is needed. Please type a valid integer after 'limit='", e)
        #                         user_interface()
        #             elif by_author_commands[0] in each_parameter:
        #                 pass
        #             else:
        #                 print("Command not recognized: ", response)
        #                 user_interface()
        #     else:
        #         print("Command not recognized: ", response)
        #         user_interface()
        #     print(command_list)
        #     command_processed = blogs_by_author(command_list[0], command_list[1])

        elif "wipe" in response_list:
            if "refresh" in response_list:
                global MAX_STALENESS
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


if __name__ == "__main__":
    user_interface()
