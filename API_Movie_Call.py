'''
API Calls TheMovieDatabase and returns a list of movies from a sorted based on a given
year, month, and day and returns a list of 20 movies.

The first movie in the list will be the closest to the exact day provided and that
movie will be returned to the API Manager. 

'''
import os
import requests
import API_Response


# Gets the API key from my local system variables.
key = os.environ.get('MOVIE_KEY')

# Base URL for discovering movies.
movie_discover_url = 'https://api.themoviedb.org/3/discover/movie?'
# URL for the images, w500 is not part of the base url, but it is the max width for a poster.
movie_images_url = 'https://image.tmdb.org/t/p/w500/'

movie_api_response = API_Response.API_Response() # Create a global API Response object so the movie functions can write to it. 

def movie_call(date):
    
    year, month, day = date.split('-') # Date is expected in YYYY-MM-DD format.
    query =set_api_discover_params(year, month, day, key)
    data = api_movie_request(movie_discover_url, query)
    movie_raw = get_movie_results(data)
    # movie_title, movie_overview, movie_poster_path = get_movie_details(movie_raw)
    # movie_img_link = get_movie_image(movie_poster_path)
    get_movie_details(movie_raw)

    return movie_api_response

def set_api_discover_params(year, month, day, key) -> dict:
    '''
    Takes a date object seperated by components and an API key and returns the 
    api call query parameters.
    '''
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
    try:
        response = requests.get(url, params=query)
        data = response.json()
        return data

    except Exception as ex:
        print(f'URL Response Error. {ex}')
        movie_api_response.connection_error = ex
    
    

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

def get_movie_details(movie_dict) -> dict:
    '''
    Takes one movie and returns its title, poster image path, and an overview of what the movie as a dictionary.
    '''
    
    movie_poster_path = movie_dict['poster_path']
    movie_poster_url = get_movie_image(movie_poster_path) # Call gets full image url path.
    movie_api_response.data = {
        'title': movie_dict['title'],
        'desc': movie_dict['overview'],
        'poster': movie_poster_url
    }

def get_movie_image(poster_path) -> str:
    '''
    Takes the movies poster path, joins it with the base image URL and returns a path to the movie poster.
    '''
    movie_poster_url = f'{movie_images_url}{poster_path}'
    return movie_poster_url
    

#TODO Some movies do not have poster paths, and some movies are straight to DVD. Need to add some functions to search through the list of 20 movies
# Think maybe it should return the highest rated movie from the given day with a poster link. 

if __name__ == '__main__':
    movie_call()