from secrets import plotly_key, plotly_username
import sqlite3 as sqlite
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import string
plotly.tools.set_credentials_file(username=plotly_username, api_key=plotly_key)


db_name = "blogs.db"


def process_tags(orderby="", desc="DESC", limit=None):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    base_statement = "SELECT Tags.TagName, Tags.NumberUsed FROM Tags"
    tag_names = []
    tag_count = []

    if orderby == "Alpha":
        statement = " ORDER BY Tags.TagName"
        base_statement += statement
        if desc == "ASC":
            statement = " ASC"
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
            base_statement += " DESC"
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
        if desc == "ASC":
            statement = " ASC"
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
            base_statement += " DESC"
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


def process_authors(orderby="Count", desc="DESC", limit_authors=None):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    base_statement = "SELECT Authors.Name, Authors.NumberBlogs FROM Authors"
    authors = []
    values = []

    if orderby == "Alpha":
        statement = " ORDER BY Authors.Name"
        base_statement += statement
        if desc == "ASC":
            statement = " ASC"
            base_statement += statement
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
        else:
            base_statement += " DESC"
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
    else:
        statement = " ORDER BY Authors.NumberBlogs"
        base_statement += statement
        if desc == "ASC":
            statement = " ASC"
            base_statement += statement
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
        else:
            base_statement += " DESC"
            if limit_authors is not None:
                statement = " LIMIT {}".format(int(limit_authors))
                base_statement += statement
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
            else:
                execute = cur.execute(base_statement)
                results = execute.fetchall()
                for result in results:
                    authors.append(result[0])
                    values.append(result[1])
    print("{:<30.25} | {:<5} \n".format("Author", "Count"))
    for result in results:
        print("{:<30.25} | {:<5}".format(result[0], result[1]))
    conn.close()
    return authors, values


def authors_pie_chart(authors, values):
    trace = go.Pie(labels=authors, values=values)
    py.plot([trace], filename="authors_pie_chart", auto_open=True)


def process_comments(limit=None):
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    dates = []
    total_comments_per_month = []

    if limit is not None:
        statement = "SELECT Blogs.Date, Blogs.Comments FROM Blogs ORDER BY Blogs.Id ASC"
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
            if len(dates) == limit:
                break
        conn.close()
        return dates, total_comments_per_month
    else:
        statement = "SELECT Blogs.Date, Blogs.Comments FROM Blogs ORDER BY Blogs.Id DESC"
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

    py.plot(data, filename='line-mode', auto_open=True)


def images_processor():
    conn = sqlite.connect(db_name)
    cur = conn.cursor()
    blogsites = []
    img_counts = []

    statement = "SELECT BlogSites.Name, Blogs.Images FROM Blogs JOIN BlogSites WHERE Blogs.BlogSite = BlogSites.Id"
    execution = cur.execute(statement)
    results = execution.fetchall()
    for result in results:
        blogsites.append(result[0])
        img_counts.append(result[1])
    conn.close()
    return blogsites, img_counts


def images_histogram(blogsites, img_counts):
    data = [
        go.Histogram(
            histfunc="count",
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

    py.plot(data, filename='binning function', auto_open=True)


# user interface

def user_interface(input):

    pass


# data = process_tags(desc="ASC", limit=10)
# tags_bar_graph(data[0], data[1])

# auth_data = process_authors("ASC", limit_authors=20)
# authors_pie_chart(auth_data[0], auth_data[1])

# results = process_comments(1)
# comments_line_graph(results[0], results[1])

# results = images_processor()
# images_histogram(results[0], results[1])
