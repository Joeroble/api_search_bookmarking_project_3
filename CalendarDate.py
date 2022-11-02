import datetime
from datetime import datetime



def check_date(date):
    try: 
        check_date = datetime.fromisoformat(date)
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