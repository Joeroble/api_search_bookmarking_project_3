import datetime
from datetime import date, datetime
import API_Response

class CalanderDate:
    """Represents API information to be used for calls from the user and stores that information
    for easier use."""

    def __init__(self,date):
        self.date = date # Date is expected in YYYY-MM-DD format.
    
    def get_date_parts(self):
        year, month, day = self.date.split('-')
        return (year, month, day)
    
    def get_date_month_day_str(self):
        year, month, day = self.get_date_parts()
        datetime_date = datetime(int(year), int(month), int(day))
        return datetime_date.strftime("%B %d")
   
    def __str__(self):
        return f'Year: {self.year}, Month: {self.month}, Day: {self.day}'

    def check_date(self,date):
        
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
        year, month, day = date.split('-')
        return (year, month, day)

def get_date_month_day_str(date):
        year, month, day = get_date_parts(date)
        datetime_date = datetime(int(year), int(month), int(day))
        return datetime_date.strftime("%B %d")