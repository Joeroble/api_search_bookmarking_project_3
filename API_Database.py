import sqlite3 

def setup_db():
    '''
    Makes the database for the user.
    '''
    #Create Connection API DB
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()
    #Create DB
    #c.execute("CREATE DATABASE API")
    
    #Create The DB
    table_sql = "CREATE TABLE IF NOT EXISTS API_Results (Date TEXT PRIMARY KEY, Movie_Title TEXT, Movie_Url TEXT, Nasa_Title, Nasa_Url TEXT, Wiki_Url TEXT)"
    c.execute(table_sql)
    
    conn.commit()
    conn.close()

def insert(bookmark_data):
    '''
    Retrive the data
    '''
    if verify_new_date(bookmark_data['date']) == False:
        conn = sqlite3.connect('API.db')  

        # Reads the individual data from a dictionary passed to the insert call.
        search_date = bookmark_data['date']
        movie_title = bookmark_data['movie_title']
        movie_url = bookmark_data['movie_img']
        nasa_title = bookmark_data['nasa_title']
        nasa_url = bookmark_data['nasa_img']
        
        #API_Manager.api_wiki_call_response(date)
        #WIKI_data = WIKI_data.data
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
        
def Select_All():
    #Creat Connection API DB
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
    print(cursor)

    results = cursor.fetchone()
    print(results)
    conn.close()
    if results[0] == 1:
        return True
    else:
        return False
    
