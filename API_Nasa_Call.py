# Calls Nasa's API to return a picture of the APOD and return the link to the image for now until Flask is setup.

'''This API ask a user to enter a specific date between beginning_date which is 1995-6-16 until today_date the current day
 and fetch a picture from APOD url and show the picture in web browser from now until we decide to use Flask '''

import requests
import datetime
from datetime import date
import webbrowser 

'''This function set a range of valid dates 
    if the user enter the right dates it will return the date_pic if not it will ask them to enter the right dates'''
    
    # Get a picture for a specific date
def get_date(): 

    today_date = date.today() 
    beginning_date = datetime.date(1995, 6, 16)  
    
    # recursively iterate over a list of False.
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
            # # Returns a date_pic based on the current date and the beginning date.
            return date_pic


'''This function Returns the url for a given date.'''
def get_url(date):
    # API KEY.
    API_KEY = '5c651pUEm3faSaZkgZ8vi2sKF7zntRQ2oXXXVhrc'
    
    # API URL for a planetary apod
    url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date}'

# Returns a URL for a given URL.
    return url

        

'''This function Fetch the image URL from the given url.'''
def fetch_image_url(url):
    
    try:
        response = requests.get(url).json()
        image_url = response['url']
        return image_url
    except:
        print('Error extracting image')
        return 'except'




'''This function Fetch image from webbrowser if it exists.'''
def main():

    user_date = get_date()
    api_url = get_url(user_date)
    image_url = fetch_image_url(api_url)
    
    if not image_url == 'except':
        try:
            webbrowser.open(image_url)  # "for now" to open a pic in a web browser 
            
            print('Success')
            
        except: 
            print('error opening image')
        
    
main()
