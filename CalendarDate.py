import datetime
from datetime import date, datetime
import API_Response

class CalanderDate:
    """Represents API information to be used for calls from the user and stores that information
    for easier use."""

    def __init__(self,str_date):
        self.str_date = str_date # Date is expected in YYYY-MM-DD format.
    
    def get_date_parts(self):
        year, month, day = self.str_date.split('-')
        return (year, month, day)
    
    def get_date_month_day_str(self):
        year, month, day = self.get_date_parts()
        datetime_date = datetime(int(year), int(month), int(day))
        return datetime_date.strftime("%B %d")
   
    def __str__(self):
        return f'Year: {self.year}, Month: {self.month}, Day: {self.day}'

    def check_date(self,str_date):
        
        today_date = date.today() 
        beginning_date = datetime.date(1995, 6, 16)  


        # Create Object of API Response
        response = API_Response.API_Response()

        # Checks if the date is within the beginning_date and today_date.
        if not (date <= today_date and date >= beginning_date):
            response.user_error = 'Error with the date provided by user, please ensure date is not in the future.'

            
            # Returns a date based on the current date and the beginning date.
        return response.user_error

def get_date_parts(date):
    try:
        year, month, day = date.split('-')
        return (year, month, day)
    except:
        # TODO Add some logging. 
        return ('1995', '06', '16')

def get_date_month_day_str(date):
    year, month, day = get_date_parts(date)
    datetime_date = datetime(int(year), int(month), int(day))
    return datetime_date.strftime("%B %d")

def get_date_for_display(date):
    year, month, day = get_date_parts(date)
    date_to_display = datetime(int(year), int(month), int(day))
    return date_to_display.strftime("%B %d %Y")

def check_date_limits(date):
    '''
    Checks each part of the date starting with year, then month, then day to make sure it is not before June 16th 1995

    If the day is before that day it will return the day June 16th 1995.
    '''
    year, month, day = get_date_parts(date)
    if int(year) > 1995: # if it is greater than 1995 we know that they are not going to hit the lower limit
        return date
    elif int(year) == 1995:
        if int(month) > 6:
            return date
        elif int(month) == 6:
            if int(day) >= 16:
                return date
            else:
                #TODO Logging?
                return '1995-06-16' # The limiter date
        else:
            return '1995-06-16'
    else:
        return '1995-06-16'