import datetime
from datetime import date, datetime


def check_date(date):
        
        today_date = date.today() 
        beginning_date = datetime.date(1995, 6, 16)  

        # Checks if the date is within the beginning_date and today_date.
        if not (date <= today_date and date >= beginning_date):
           acceptable_date = True

        else:    
            acceptable_date = False
        return acceptable_date
   
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

def check_date_limits(date):
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