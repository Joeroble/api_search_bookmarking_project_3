# Calls Nasa's API to return a picture of the APOD and return the link to the image for now until Flask is setup.

"""This API ask a user to enter a specific date between beginning_date which is 1995-6-16 until today_date the current day
 and fetch a picture from APOD url and show the picture in web browser from now until we decide to use Flask """

from urllib import response
from wsgiref.simple_server import server_version
import requests
import datetime
from datetime import date
#import webbrowser 
import os 
from pprint import pprint
from flask import Flask

app = Flask(__name__)

"""This function set a range of valid dates 
    if the user enter the right dates it will return the date_pic if not it will ask them to enter the right dates"""





# Get a picture for a specific date
def get_date(): 

    today_date = date.today() 
    beginning_date = datetime.date(1995, 6, 16)  
    
    
    while True:
        
        print('Enter the following so we can get you a picture for the specific date you choose: ')
        # Prints a warning message if the date is between the beginning and today.
        print(f'Make sure date is between {beginning_date} and {today_date}')


        # ask user inputs and return int
        year = int(input('Enter year: '))
        month = int(input('Enter month: '))
        day = int(input('Enter day: '))


        # Obtains a local datetime. date object representing the current date.
        date_pic = datetime.date(year, month, day)



        # Checks if the date_pic is within the beginning_date and today_date.
        if date_pic <= today_date and date_pic >= beginning_date:
            
            # Returns a date_pic based on the current date and the beginning date.
            return date_pic





@app.route('/')

def fetch_url(date):
    
    try:
        key = os.environ.get('NASA_KEY')
    # API URL for a planetary apod
        query = {'api_key':key,'date': date}
        url = f'https://api.nasa.gov/planetary/apod'

        response = requests.get(url,params=query).json()
        
<<<<<<< Updated upstream
        paramaters = {
        "date":response ['date'],
        "explanation": response ['explanation'],
        "hdurl": response['hdurl'],
        "media_type": response ['media_type'],
        "service_version": response ['service_version'],
       "title": response ['title'],
       "url": response ['url']
        }
        return paramaters

    except:
        print('Error extracting image')
        return 'except' 
=======
        """
        Check if the data is accurate by date 
        """
        calendar2 = CalendarDate.CalendarDate(response['date'])
        Date = calendar2.get_date()       
        
        
        
        if  Date == date:
            nasa_api_response.data = response
        return nasa_api_response
>>>>>>> Stashed changes


def main():

    user_date = get_date()
    params = fetch_url(user_date)
    
    pprint(params)
    if not fetch_url == 'except':
        try:
            app.run(debug=True,port = 2000)
            print('Success')
            
        except: 
            print('error opening image')
        
if __name__   == "__main__":
    main()
