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
# Day month year need to be in string format because the API is expecteing a ####-##-## format for Year-Month-Day
##################
year = '2010'
month = '08'
day = '23'
##################

# Gets the API key from my local system variables.
key = os.environ.get('MOVIE_KEY')

# Base URL for discovering movies.
movie_discover_url = 'https://api.themoviedb.org/3/discover/movie?'
# URL for the images, w500 is not part of the base url, but it is the max width for a poster.
movie_images_url = 'https://image.tmdb.org/t/p/w500/'

def movie_call(date):
    year, month, day = split_date(date)
    query =set_api_discover_params(year, month, day, key)
    data = api_movie_request(movie_discover_url, query)
    movie_raw = get_movie_results(data)
    # movie_title, movie_overview, movie_poster_path = get_movie_details(movie_raw)
    # movie_img_link = get_movie_image(movie_poster_path)
    movie_info = get_movie_details(movie_raw)

    # print(movie_title)
    # print(movie_overview)
    # print(movie_img_link)
    return movie_info

def split_date(date):
    date_split = date.split('-')
    return date_split[0], date_split[1], date_split[2]

def set_api_discover_params(year, month, day, key) -> dict:
    '''
    Takes a date object seperated by components and an API key and returns the 
    api call query parameters.
    '''
    # TODO potential if statement to check year, month, day are type string.
    # Query for discovery
    query = {'api_key':key, 
    'language':'en-US', # Language sets the movies title string so we return english version names of movies
    'sort_by':'release_date.desc', # Sorts the results of the API Call.
    'include_adult':'false',
    'include_video':'false',
    'page':'1', # Page represents what page of the results will be looked at.
    'primary_release_year':year, 
    'primary_release_date.lte':f'{year}-{month}-{day}',
    'vote_average.gte':'3', 
    'with_original_language':'en'}

    return query

def api_movie_request(url, query):
    '''
    Takes a url and a query string and returns json data.
    '''

    data = requests.get(url, params=query).json()

    return data

def get_movie_results(json_data) -> dict:
    '''
    Takes json data returned from an api request and returns one movie
    (Break down into two functions? Might make unit testing easier.)
    '''
    movie_result_list = json_data['results']
    if len(movie_result_list) > 0:
        return movie_result_list[0]
    else:
        return 'Your movie is in another castle.'

def get_movie_details(movie_dict):
    '''
    Takes one movie and returns its title, poster image path, and an overview of what the movie is.
    '''
    # movie_title = movie_dict['title']
    # movie_desc = movie_dict['overview']
    movie_poster_path = movie_dict['poster_path']
    movie_poster_url = get_movie_image(movie_poster_path)
    return {
        'title': movie_dict['title'],
        'desc': movie_dict['overview'],
        'poster': movie_poster_url
    }
    # return movie_title, movie_desc, movie_poster_path

def get_movie_image(poster_path):
    '''
    Takes the movies poster path, joins it with the base image URL and returns a path to the movie poster.
    '''
    movie_poster_url = f'{movie_images_url}{poster_path}'
    return movie_poster_url

# Is this needed, should API Call be checking the date again or should this check be happening before the date is passed
# To the call.
def check_date_format(year, month, day) -> bool:
    '''
    Checks to make sure the dates passed are a String before formatting the query params
    '''
    if type(year) != str or type(month) != str or type(day) != str:
        return False
    else:
        return True
    

#TODO Some movies do not have poster paths, and some movies are straight to DVD. Need to add some functions to search through the list of 20 movies
# Think maybe it should return the highest rated movie from the given day with a poster link. 

if __name__ == '__main__':
    movie_call()