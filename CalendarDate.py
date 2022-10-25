import datetime
from datetime import date
import API_Response

class CalanderDate:
    """Represents API information to be used for calls from the user and stores that information
    for easier use."""

    def __init__(self,date):
        self.date = date # Date is expected in YYYY-MM-DD format.
    
    def get_date(self):
        year , month , day = self.date.split('-')
        return datetime.date(int(year),int(month),  int(day))
   
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