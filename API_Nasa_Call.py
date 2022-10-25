"""
API calls nasa url to return a picture of the day and its information(url, date, copyright, explanatian, and title)based on the given date 
then return it to API Manager.

"""

import requests
import os 
from pprint import pprint
import API_Response
import CalendarDate

""" Create a global API Response object so the nasa functions can write to it."""

nasa_api_response = API_Response.API_Response()

def nasa_call(date):    
    try: 
        calendar = CalendarDate.CalendarDate(date)
        date = calendar.get_date()    
        """
        check on the date it is in the right range between today date and beginning_date 
        return the user_error 
        (if there is an error it will print an error ,else it will return None)
        
        """

        nasa_api_response.user_error = calendar.check_date(date)
        
        """ Gets the API key from my local system variables."""
        key = os.environ.get('NASA_KEY')
        
        """ Set the api key and date."""
        query = {'api_key':key,'date': date}
        
        """ URL for apod planetary."""
        url = f'https://api.nasa.gov/planetary/apod'

        response = requests.get(url,params=query).json()
        
        """
        Check if the data is accurate  by date 
        """
        calendar2 = CalendarDate.CalendarDate(response['date'])
        Date = calendar2.get_date()       
        
        
        
        if  Date == date:
            nasa_api_response.data = response
        return nasa_api_response


    except Exception as e:
            nasa_api_response.connection_error = e
            return nasa_api_response
