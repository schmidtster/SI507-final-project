## Data Sources:

UMICH Library Blog Website: [https://www.lib.umich.edu/blogs][https://www.lib.umich.edu/blogs]

#### secrets.py:
    
In order to get plotly graphs working, you will need to use a separate file called secrets.py. This file should
contain the plotly_key and plotly_username. Sign up for a plot.ly account and visit 
https://plot.ly/python/getting-started/ to install plotly modules necessary to run use graphs.
Use the requirements.txt to see all modules necessary to run the program.
    
## Description:

My code is structured into two main python programs and one unittest program.
    
#### lib_blog.py:

Description: lib_blog.py scrapes the UMICH Library Blog website and gathers information about each blog posted.
            
##### PROCESSING FUNCTIONS:

_get_blogs()_: This function scrapes the 99 pages of blogs on the UMICH library website. From those pages, it
gathers Title, BlogURL, Author, AuthorURL, Date, Description, BlogSite, BlogSiteURL. It then passes this
information into the BlogPost class.

_clean_database()_: This function deletes any previous database containing tables: Blogs, BlogSites, Tags,
Associations, and Authors. It then reconstructs the tables with the necessary fields.

_enter_data_to_db()_: This function takes the to_json() output of a class instance of BlogPost and inputs the 
data fields for each table (except TagAssociations) for each blog post.

_update_records()_: This function: deletes duplicate tags, authors, and blogsites from their respective
tables; establishes relations for tags, blogsites, authors; fills in data for TagAssociations; and fills in
data for number of times tags were used and number of blogs authors published.

##### CLASSES:

__BlogPost__: Inputs are information gathered from scraping UMICH blog pages. It crawls into each individual blog
page and extracts more information. Class functions include: to_json(): which outputs a json dictionary and
__str__(): which displays basic information about each blog.

#### user_interface.py:

Description: Processes queries for the database and displays information both in the terminal and through
plotly.

##### PROCESSING FUCNTIONS:

_user_interface()_: This function takes commands entered into the command line and filters them to run
the functions outlined. Filters commands and parameters with a series of lists.

**tags functions**: _process_tags()_ and _tags_bar_graph()_ - Retrieve information from the database and display it 
with plotly bar graph.

**authors functions**: _process_authors()_ and _authors_pie_graph()_ - Retrieve information about authors from the
database and display it using plotly pie graph.

**comments functions**: _process_comments()_ and _comments_line_graph()_ - Retrieve information about comment counts
per month from the database and display it using a plotly line graph.

**images functions**: _process_images()_ and _images_histogram()_ - Retrive information about the number of images
used per blog site (total) and display the total and averages as a plotly histogram.

#### final_proj_test.py:

Description: A series of unittests that determine if scraping, ingest of data, and user_interface are
properly configured.

##### CLASSES:

**class TestScraping(unittest.TestCase)**: Tests the scraping and crawling are working as needed.

**class TestDatabase(unittest.TestCase)**: Tests database construction and satisfactory query output.

**class TestUserInterface(unittest.TestCase)**: Tests data processing procedures and data structures needed for 
presentation.

## User Guide:
    
#### lib_blog.py

Simply run the program by using the wipe or wipe refresh commands listed below.

    
#### user_interface.py

##### tags
    
Description: A function that compares the number of tags used for x number of articles.

    Options:
        orderby="count" or "alpha" - Default is "count"
        Description: Specifies whether to order tags alphabetically by typing "Alpha" or order according to the number
        of times the tag has been used in total. Default is by database.

        desc="desc" or "asc" - Default is "desc"
        Description: Specifies whether you would like your list returned in descending or ascending order. The default
        is descending.

        limit=None or # - Default is None
        Description: Specifies the amount of results you want returned. The default is all results in the database.

        graph - Default is graph
        Description: Specifies if you would like a graph of the data displayed in your default web browser. It will auto
        open the graph in your browser. The default is "y" for yes.
        
Example inputs: 
        
    "tags alpha asc limit=5"
    "tags limit=15 graph"

##### authors
    
Description: A function that lists authors names, their urls, and the amount of blogs they have posted.

    Options:
        orderby="count" or "alpha" - Default is "count"
        Description: Specifies if the information displayed is ordered by the total number of blogs an author has
        published or lists authors name alphabetically, starting with their first name.

        desc="desc" or "asc" - Default is "desc"
        Description: Specifies whether the results returned should be in descending or ascending order. The default is
        descending.

        limit=None or # - Default is None
        Description: Specifies the amount of results returned. The default is all the results in the database.

        graph - Default is graph
        Description: Specifies if you would like a graph of the data displayed in your default web browser. It will auto
        open the graph in your browser. The default is "y" for yes.
Example inputs:

    "authors alpha asc limit=10 graph"
    "authors limit=10 graph"

##### comments
    
Description: A function that returns the amount of comments made per month on all of the blogs published.

    Options:
        limit=None or # - Default is None
        Description: Specifies the amount of results returned. The default is all the results in the database.

        graph - Default is graph
        Description: Specifies if you would like a graph of the data displayed in your default web browser. It will auto
        open the graph in your browser. The default is "y" for yes.
Example inputs:

    "comments limit=10"
    "comments graph"

##### images
    
Description: A function that returns the total number of images used for all posts made by a single blog site.

    Options:
        graph - Default is graph
        Description: Specifies if you would like a graph of the data displayed in your default web browser. It will auto
        open the graph in your browser. The default is "y" for yes.
Example Inputs:

    "images graph"
    "images"

##### most_recent
    
Description: A function that returns the most recent blogs to be published on the Library Blog site.

    Options:
        limit=None or # - Default is None
        Description: Specifies the amount of results returned. The default is all the results in the database.
Example inputs:

    "most_recent limit=15"
    "most_recent"

##### wipe
    
Description: A function that wipes the database and rescrapes the UMICH Library Blog site

    Options:
    refresh - Default is False
    Description: Specifies if you want to scrape the website for new data or receive cached data. Using refresh will
    scrape and crawl the UMICH Library Blog website, so it will take around 10 minutes to get the new data.
Example Input:
    
    "wipe"
    "wipe refresh"

##### help
    
Description: A command that will bring up all available commands and their parameters.

Example input:

    "help"

##### exit
    
Description: Exit the program.

Example input:

    "exit"


[https://www.lib.umich.edu/blogs]: https://www.lib.umich.edu/blogs