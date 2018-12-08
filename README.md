Data Sources:

    UMICH Library Blog Website: https://www.lib.umich.edu/blogs

secrets.py: 
    
    In order to get plotly graphs working, you will need to use a separate file called secrets.py. This file should
    contain the plotly_key and plotly_username. Sign up for a plot.ly account and visit 
    https://plot.ly/python/getting-started/ to install plotly modules necessary to run use graphs.
    Use the requirements.txt to see all modules necessary to run the program.
    
Description:

    My code is structured into two main python programs, described below:
    
        lib_blog.py:
            Description: lib_blog.py scrapes the UMICH Library Blog website and gathers information about each blog
            posted.
            
            PROCESSING FUNCTIONS:
            get_blogs(): This function scrapes the 99 pages of blogs on the UMICH library website. From those pages, it
            gathers Title, BlogURL, Author, AuthorURL, Date, Description, BlogSite, BlogSiteURL. It then passes this
            information into the BlogPost class.
            
            clean_database(): This function deletes any previous database containing tables: Blogs, BlogSites, Tags,
            Associations, and Authors. It then reconstructs the tables with the necessary fields.
            
            enter_data_to_db(): This function takes the to_json() output of a class instance of BlogPost and inputs the 
            data fields for each table (except TagAssociations) for each blog post.
            
            update_records(): This function: deletes duplicate tags, authors, and blogsites from their respective
            tables; establishes relations for tags, blogsites, authors; fills in data for TagAssociations; and fills in
            data for number of times tags were used and number of blogs authors published.
            
            CLASSES:
            BlogPost: Inputs are information gathered from scraping UMICH blog pages. It crawls into each individual blog
            page and extracts more information. Class functions include: to_json(): which outputs a json dictionary and
            __str__(): which displays basic information about each blog.
        
        user_interface.py:
            Description: Processes queries for the database and displays information both in the terminal and through
            plotly.
            
            PROCESSING FUCNTIONS:
            user_interface(): This function takes commands entered into the command line and filters them to run
            the functions outlined. Filters commands and parameters with a series of lists.
            
            tags functions: process_tags() and tags_bar_graph() - Retrieve information from the database and display it 
            with plotly bar graph.
            
            authors functions: process_authors() and authors_pie_graph() - Retrieve information about authors from the
            database and display it using plotly pie graph.
            
            comments functions: process_comments() and comments_line_graph() - Retrieve information about comment counts
            per month from the database and display it using a plotly line graph.
            
            images functions: process_images() and images_histogram() - Retrive information about the number of images
            used per blog site (total) and display the total and averages as a plotly histogram.
            
        final_proj_test.py:
            Description: A series of unittests that determine if scraping, ingest of data, and user_interface are
            properly configured.
            
            CLASSES:
            
            class TestScraping(unittest.TestCase): Tests the scraping and crawling are working as needed.
            
            class TestDatabase(unittest.TestCase): Tests database construction and satisfactory query output.
            
            class TestUserInterface(unittest.TestCase): Tests data processing procedures and data structures needed for 
            presentation.

User Guide:
    
    lib_blog.py
    FILL IN MORE HERE
    
    user_interface.py
    Commands available:
    tags
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
    
    authors
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
    
    comments
        Description: A function that returns the amount of comments made per month on all of the blogs published.
    
        Options:
            limit=None or # - Default is None
            Description: Specifies the amount of results returned. The default is all the results in the database.
    
            graph - Default is graph
            Description: Specifies if you would like a graph of the data displayed in your default web browser. It will auto
            open the graph in your browser. The default is "y" for yes.
    
    images
        Description: A function that returns the total number of images used for all posts made by a single blog site.
    
        Options:
            graph - Default is graph
            Description: Specifies if you would like a graph of the data displayed in your default web browser. It will auto
            open the graph in your browser. The default is "y" for yes.
    
    most_recent
        Description: A function that returns the most recent blogs to be published on the Library Blog site.
    
        Options:
            limit=None or # - Default is None
            Description: Specifies the amount of results returned. The default is all the results in the database.
    
    help
        Description: A command that will bring up all available commands and their parameters.
    
    exit
        Description: Exit the program.