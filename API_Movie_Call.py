'''
API Calls TheMovieDatabase and returns a list of movies from a sorted based on a given
year, month, and day and returns a list of 20 movies.

The first movie in the list will be the closest to the exact day provided and that
movie will be returned to the API Manager. 

'''
import os
import requests
from pprint import pprint # Imported pprint of testing, should be removed once UI display is hooked up

# Hard coded year month and day will be replaced once we are able to pass
# a date object that these variables can be extrated from. 
##################
year = '2008'
month = '10'
day = '22'
##################

# Gets the API key from my local system variables.
key = os.environ.get('MOVIE_KEY')

# Base URL for discovering movies.
movie_url = 'https://api.themoviedb.org/3/discover/movie?'

# Query for discovery
query = {'api_key':key, 
    'language':'en-US', # Language sets the movies title string so we return english version names of movies
    'sort_by':'release_date.desc', # Sorts the results of the API Call.
    'include_adult':'false',
    'page':'1', # Page represents what page of the results will be looked at.
    'primary_release_year':year, 
    'primary_release_date.lte':f'{year}-{month}-{day}',
    'vote_average.gte':'3', 
    'with_original_language':'en'}

data = requests.get(movie_url, params=query).json()
movie_results_list = data['results']

for movie in movie_results_list:
    pprint(movie)
