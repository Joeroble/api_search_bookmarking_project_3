import sqlite3 


"""Create the database if it does not exist."""
def setup_db():
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()
    
    table_sql = "CREATE TABLE IF NOT EXISTS API_Results (Date TEXT PRIMARY KEY, Movie_Title TEXT, Movie_Url TEXT, Nasa_Title, Nasa_Url TEXT, Wiki_Url TEXT)"
    c.execute(table_sql)
    
    conn.commit()
    conn.close()


"""Takes the data from the ui from the API callssuch as the saved search_date, the movie_title,
movie_url, nasa_title, nasa_url, and then inserts the new bookmark being saved by the user using the search_date is
primary key. Will not add a bookmark with a date already added."""
def insert(bookmark_data):

    if not verify_new_date(bookmark_data['date']):
        conn = sqlite3.connect('API.db')  

        # Reads the individual data from a dictionary passed to the insert call.
        search_date = bookmark_data['date']
        movie_title = bookmark_data['movie_title']
        movie_url = bookmark_data['movie_img']
        nasa_title = bookmark_data['nasa_title']
        nasa_url = bookmark_data['nasa_img']
        wiki_url = bookmark_data['wiki_link']
        
        #Insert Data in DB
        bookmark_data = (search_date, movie_title, movie_url, nasa_title, nasa_url, wiki_url)
        
        c = conn.cursor()
        
        # Executing the sql Query
        c.execute("INSERT into API_Results values(?, ?, ?, ?, ?, ?)",bookmark_data)

        # Commit method to make changes in the table
        conn.commit()
        conn.close()
    else:
        pass # We do not want to insert a record that already exists.
        

"""Create Connection API DB, runs a query using SELECT * from the API_Results table within the DB, which then stores it in the table variable
and returns it to the UI for display."""
def Select_All():
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()
    conn.commit()

    c.execute("SELECT * FROM API_Results ")
    table = c.fetchall()
    
    conn.close()
    
    return table

def verify_new_date(search_date):
    """
    Checks to see if a date has already been saved to the database by searching the database
    for the submitted date, if it already exists the function returns false -> not a new date

    or if it does not exist it returns True -> is a new date. 
    """
    conn = sqlite3.connect('API.db')
    
    cursor = conn.execute('SELECT EXISTS (SELECT * FROM API_Results WHERE Date = (?));', (search_date, ))
    

    results = cursor.fetchone()
    conn.close()
    if results:
        return True
    else:
        return False
    
