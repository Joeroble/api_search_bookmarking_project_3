'''
API Manager is passed a user created Calander date object from the UI
and passes that data onto each of the three API_calls. Each API_Call 
then returns its result back to API Manager. 

API Manager can be called by the UI to retrieve those results for display. 
'''
import API_Wiki_Call

"""api call and resposne for Wiki, it will bring in the user_calender_date passed to it from ui/main, call upon API_Wiki_Call to make the API connection,
get the response, and then check the response with the api_response_handling.  This will then return the checked response back to ui/main."""
def api_wiki_call_response(user_calender_date):
    api_response = API_Wiki_Call.API_Wiki_Call(user_calender_date)
    # Note - The api_response_handling is in another PR at the moment, when both are merged, this code will work.
    api_response_checked = api_response_handling(api_response)
    return api_response_checked
