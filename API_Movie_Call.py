'''API Calls TheMovieDatabase and returns a list of movies from a given date and picks one at random.'''
import os
import requests
from pprint import pprint


year = '2008'
month = '10'
day = '22'
key = os.environ.get('MOVIE_KEY')
movie_url = 'https://api.themoviedb.org/3/discover/movie?'
query = {'api_key':key, 
    'language':'en-US', 
    'sort_by':'release_date.desc',
    'include_adult':'false', 
    'page':'1', 
    'primary_release_year':year, 
    'primary_release_date.lte':f'{year}-{month}-{day}',
    'vote_average.gte':'3',
    'with_original_language':'en'}

data = requests.get(movie_url, params=query).json()
movie_results_list = data['results']
for movie in movie_results_list:
    pprint(movie)
