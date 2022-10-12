'''
API Manager is passed a user created Calander date object from the UI
and passes that data onto each of the three API_calls. Each API_Call 
then returns its result back to API Manager. 

API Manager can be called by the UI to retrieve those results for display. 
'''

"""This will take the data that was retrieved or not from the API, using a return of False for the exception.  It will return an appropriate message if 
there was a connection error, of if content was not found.  This is setup with the expectation that each API call will use try and except blocks in for the
error handling, and None if content was not found."""
def api_response_handling(api_response):
    if api_response:
        return api_response
        
    elif api_response == False:
        api_error = 'There was an error connecting to the API'
        return api_error

    else:
        content_not_found = 'No content was found with that date'
        return content_not_found
