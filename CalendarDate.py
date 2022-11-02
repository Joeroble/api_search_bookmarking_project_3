import datetime
from datetime import datetime

"""CalendarDate has functions that handle checking that it is a valid date, separating the date out into parts, formatters so the dates match what the API calls
require and the date for display."""


def check_date(user_date):
    try: 
        check_date = datetime.fromisoformat(user_date)
        today_date = datetime.today() 
        beginning_date = datetime(1995, 6, 16)  

        # Checks if the date is within the beginning_date and today_date.
        if (check_date <= today_date and check_date >= beginning_date):
            acceptable_date = True

        else:    
            acceptable_date = False
        return acceptable_date
    except Exception as e:
        return False

   
def get_date_parts(user_date):
    try:
        year, month, day = user_date.split('-')
        return (year, month, day)
    except:
        # TODO Add some logging. 
        return ('1995', '06', '16')

def get_date_month_day_str(user_date):
    year, month, day = get_date_parts(user_date)
    datetime_date = datetime(int(year), int(month), int(day))
    return datetime_date.strftime("%B %d")

def get_date_for_display(user_date):
    year, month, day = get_date_parts(user_date)
    date_to_display = datetime(int(year), int(month), int(day))
    return date_to_display.strftime("%B %d %Y")
