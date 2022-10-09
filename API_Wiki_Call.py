
""""Using Wikipedia's API to return the events that happened on the day chosen by the user."""

import requests
from pprint import pprint

# user_date is currently hardcoded, this will take a variable later that is passed to it from ui.py.
user_date = 'October 9'

query = {'action':'opensearch', 'namespace':0, 'search': user_date, 'limit':1}


url ='https://en.wikipedia.org/w/api.php'

data = requests.get(url, params = query).json()

pprint(data[3])