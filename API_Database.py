import sqlite3 
import API_Manager

def insert(bookmark_data):
    
    #Create Connection API DB
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()
    #Create DB
    #c.execute("CREATE DATABASE API")
    
    #Create The DB
    table_sql = "CREATE TABLE IF NOT EXISTS API_Results (Date TEXT PRIMARY KEY, Movie_Title TEXT, Movie_Url TEXT, Nasa_Title, Nasa_Url TEXT, Wiki_Url TEXT)"
    c.execute(table_sql)
    
    conn.commit()

    '''
    Retrive the data
    '''
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
        
def Select_All():
    #Creat Connection API DB
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()

    
    
    conn.commit()
    c.execute("SELECT * FROM API_Results ")
    Table = c.fetchall()
    return Table
    # for i in Table:
    #     print("Date: ", i[0])
    #     print("Movie Title: ", i[1])
    #     print("NASA URL: ", i[2])
    #     print("WIKI URL: ", i[3])