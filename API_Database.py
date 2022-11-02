import sqlite3 


"""Create the database if it does not exist."""
def setup_db():
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()
    
    table_sql = "CREATE TABLE IF NOT EXISTS API_Results (Date TEXT PRIMARY KEY, Movie_Title TEXT, Movie_Url TEXT, Nasa_Title, Nasa_Url TEXT, Wiki_Url TEXT)"
    c.execute(table_sql)
    
    conn.commit()
    conn.close()


"""Retrive the data from the database, and then insert the new bookmark being saved by the user."""
def insert(bookmark_data):
    conn = sqlite3.connect('API.db')  

    search_date = bookmark_data['date']
    movie_title = bookmark_data['movie_title']
    movie_url = bookmark_data['movie_img']
    nasa_title = bookmark_data['nasa_title']
    nasa_url = bookmark_data['nasa_img']
    wiki_url = bookmark_data['wiki_link']
    bookmark_data = (search_date, movie_title, movie_url, nasa_title, nasa_url, wiki_url)

    c = conn.cursor()
    c.execute("INSERT into API_Results values(?, ?, ?, ?, ?, ?)",bookmark_data)

    conn.commit()
    conn.close()
        

"""Create Connection API DB, and select all results, then return the table."""
def Select_All():
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()
    conn.commit()

    c.execute("SELECT * FROM API_Results ")
    table = c.fetchall()
    
    conn.close()
    
    return table
