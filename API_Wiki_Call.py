
""""Using Wikipedia's API to return the events that happened on the day chosen by the user."""

import requests
import API_Response


def API_Wiki_Call(user_date):

    query = {'action':'opensearch', 'namespace':0, 'search': user_date, 'limit':1}
    url ='https://en.wikipedia.org/w/api.php'

    """ This will try to get the request from wiki, if it fails for some reason, a message will print, 
     and return the error, api manager should handle errors from the API call.  Assuming it is successful, 
     and there is an item now in wiki_date_page_selection, that will then be stored in extracted_page_url, and returned. 
     If there is nothing returned, it will print a message and return None. """
    try:
            wiki_date_page_selection = requests.get(url, params = query).json()
            wiki_data_check = wiki_date_page_selection[3]
            print(wiki_data_check)
            if wiki_data_check:
                data = wiki_date_page_selection
                user_error = False
                connection_error = False
                status_description = 'Success'
                wiki_api_response = API_Response.API_Response(data, user_error, connection_error, status_description)
                return wiki_api_response
            
            else:
                data = None
                user_error = True
                connection_error = False
                status_description = 'Error with the date provided by user, please ensure date is not in the future.'
                wiki_api_response = API_Response.API_Response(data, user_error, connection_error, status_description)
                return wiki_api_response
        
    except Exception as e:
            data = None
            user_error = False
            connection_error = True
            status_description = e
            wiki_api_response = API_Response.API_Response(data, user_error, connection_error, status_description)
            return wiki_api_response

  