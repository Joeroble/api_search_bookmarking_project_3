
""""Using Wikipedia's API to return the events that happened on the day chosen by the user."""

import requests


def API_Wiki_Call(user_date):

    query = {'action':'opensearch', 'namespace':0, 'search': user_date, 'limit':1}
    url ='https://en.wikipedia.org/w/api.php'

    try:
        data = requests.get(url, params = query).json()

        if data:
            return data[3]
        
        else:
            return None
    
    except Exception as e:
        print('API connection failed', e)

  
