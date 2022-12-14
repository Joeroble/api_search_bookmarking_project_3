'''
API Manager is passed a user created Calander date object from the UI
and passes that data onto each of the three API_calls. Each API_Call 
then returns its result back to API Manager. 

API Manager can be called by the UI to retrieve those results for display. 
'''
import API_Wiki_Call
import API_Nasa_Call
import API_Movie_Call
import API_Database

"""api call and resposne for Wiki, it will bring in the user_calender_date passed to it from ui/main, call upon API_Wiki_Call to make the API connection,
get the response.  This will then return the response back to ui/main."""
def api_wiki_call_response(user_calender_date):
    wiki_api_response = API_Wiki_Call.API_Wiki_Call(user_calender_date)
    return wiki_api_response


"""api call and resposne for Nasa, it will bring in the user_calender_date passed to it from ui/main, call upon API_Nasa_Call to make the API connection,
get the response.  This will then return the response back to ui/main."""
def api_nasa_call_response(user_calender_date):
    nasa_api_response = API_Nasa_Call.nasa_call(user_calender_date)
    return nasa_api_response


"""api call and resposne for movie, it will bring in the user_calender_date passed to it from ui/main, call upon API_Movie_Call to make the API connection,
get the response.  This will then return the response back to ui/main."""
def api_movie_call_response(user_calander_date):
    movie_api_response = API_Movie_Call.movie_call(user_calander_date)
    return movie_api_response


"""Calls upon the API_Database to run its setup, which will create a database if one does not exist"""
def setup_local_database():
    API_Database.setup_db()


"""Calls upon the API_Database to save the data returned from the API calls if the user elects to do so."""
def save_to_database(bookmark_data):
    API_Database.insert(bookmark_data)


"""Calls upon the API_Database to return the currently saved bookmarks"""
def get_bookmarks():
    return API_Database.Select_All()