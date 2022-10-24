
""""Using Wikipedia's API to return the events that happened on the day chosen by the user."""

import requests
import API_Response


def API_Wiki_Call(user_date):

    query = {'action':'opensearch', 'namespace':0, 'search': user_date, 'limit':1}
    url ='https://en.wikipedia.org/w/api.php'

    wiki_api_response = API_Response.API_Response()

    """ This will try to get the request from wiki, if it fails for some reason, a message will print, 
     and return the error, api manager should handle errors from the API call.  Assuming it is successful, 
     and there is an item now in wiki_date_page_selection, that will then be stored in extracted_page_url, and returned. 
     If there is nothing returned, it will print a message and return None. """
     
    try:

            wiki_date_page_selection = requests.get(url, params = query).json()
            wiki_data_check = wiki_date_page_selection[3]

            if wiki_data_check:
                data = wiki_date_page_selection[3]
                wiki_api_response.data = data
                return wiki_api_response
            
            else:
                wiki_api_response.user_error = 'Error with the date provided by user, please ensure date is not in the future.'
                return wiki_api_response
        
    except Exception as e:
            wiki_api_response.connection_error = e
            return wiki_api_response

  