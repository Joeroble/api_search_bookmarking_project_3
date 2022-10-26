import sqlite3 
import API_Manager
def insert(date):
    
    #Create Connection API DB
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()
    #Create DB
    #c.execute("CREATE DATABASE API")
    
    #Create The DB
    c.execute("CREATE TABLE IF NOT EXISTS API_Results (Date TEXT PRIMARY KEY, Movie_Title TEXT, NASA_URL TEXT, WIKI_URL TEXT)")
    
    conn.commit()

    '''
    Retrive the data
    '''
    MOVIE_title = " Movie Title"
    NASA_data = API_Manager.api_nasa_call_response(date)
    NASA_data = NASA_data.data
    NASA_URL = NASA_data['url']
    
    #API_Manager.api_wiki_call_response(date)
    #WIKI_data = WIKI_data.data
    WIKI_URL = 'Wiki Page'
    
    #Insert Data in DB
    data = (date,MOVIE_title, NASA_URL, WIKI_URL)
    
    c = conn.cursor()

    # Executing the sql Query
    c.execute("INSERT into API_Results values(?, ?, ?, ?)",data)

    # Commit method to make changes in the table
    conn.commit()
        
def Select_All():
    #Creat Connection API DB
    conn = sqlite3.connect('API.db')   
    c = conn.cursor()

    
    
    conn.commit()
    c.execute("SELECT * FROM API_Results ")
    Table = c.fetchall()
    for i in Table:
        print("Date: ", i[0])
        print("Movie Title: ", i[1])
        print("NASA URL: ", i[2])
        print("WIKI URL: ", i[3])