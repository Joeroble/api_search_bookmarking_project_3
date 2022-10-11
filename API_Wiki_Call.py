
""""Using Wikipedia's API to return the events that happened on the day chosen by the user."""

import requests

#This main call only exists for the purposes of testing this function, 
# this will be removed in the final version as the API manager will handle the calls.
def main():
    API_Wiki_Call()
    

def API_Wiki_Call():

    #User_date will be a string that contains the date that will be used in the query string, this will be passed to the function in a later version.
    user_date = "October 9"

    query = {'action':'opensearch', 'namespace':0, 'search': user_date, 'limit':1}
    url ='https://en.wikipedia.org/w/api.php'

    """ This will try to get the request from wiki, if it fails for some reason, a message will print, 
     and return the error, api manager should handle errors from the API call.  Assuming it is successful, 
     and there is an item now in wiki_date_page_selection, that will then be stored in extracted_page_url, and returned. 
     If there is nothing returned, it will print a message and return None. """
    try:
        wiki_date_page_selection = requests.get(url, params = query).json()

        if wiki_date_page_selection:
            extracted_page_url = wiki_date_page_selection[3]
            return extracted_page_url
        
        else:
            print('No page was found with that date')
            return None
    
    except Exception as e:
        print('API connection failed', e)
        return e

  
main()