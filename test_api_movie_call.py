import unittest
from unittest import TestCase
from unittest.mock import patch

import API_Movie_Call
import CalendarDate


class Test_API_Movie_call(TestCase):

    @patch('requests.Response.json')
    def test_api_movie_call_data_returned(self, mock_movie_json):
        mock_movie_date = '1995-06-16'
        mock_calendar_date = CalendarDate.get_date_parts(mock_movie_date)
        example_movie_api_response = {
            'results':[{'adult': False, 
            'backdrop_path': None, 
            'genre_ids': [28, 878], 
            'id': 254575, 
            'original_language': 'en', 
            'original_title': 'Memory Run', 
            'overview': 'The year is 2015, and big brother is everywhere. The search for immortality is over.' 
            'Science has finally achieved the impossible, undermining the most basic aspect of life:' 
            'that Mind, Body, and Soul must be one, Those who benefit from this new technology will' 
            'wake up to a new and youthful beginning - the rest of humankind must live a' 
            'bad dream and wake up to a living nightmare that goes beyond life, beyond death, '
            'and beyond redemption.', 
            'popularity': 2.109, 
            'poster_path': '/lhihUhg5ZehO1KHRIIDxz9ka0CZ.jpg', 
            'release_date': '1995-06-16',
            'title': 'Memory Run',
            'video': False, 
            'vote_average': 5.3, 'vote_count': 3}]}
        expected_movie_api_response_data = {
        'title': 'Memory Run', 
        'desc': 'The year is 2015, and big brother is everywhere. The search for immortality is over.'
        'Science has finally achieved the impossible, undermining the most basic aspect of life:that Mind, Body, and Soul must be one, '
        'Those who benefit from this new technology willwake up to a new and youthful beginning - ' 
        'the rest of humankind must live abad dream and wake up to a living nightmare '
        'that goes beyond life, beyond death, and beyond redemption.', 
        'poster': 'https://image.tmdb.org/t/p/w500//lhihUhg5ZehO1KHRIIDxz9ka0CZ.jpg'}
        mock_movie_json.side_effect = [example_movie_api_response]
        movie_api_response = API_Movie_Call.movie_call(mock_calendar_date)
        self.maxDiff = None
        print(movie_api_response.data)
        self.assertEqual(expected_movie_api_response_data, movie_api_response.data)



    @patch('API_Movie_Call.api_movie_request', side_effect=Exception)
    def test_api_wiki_call_connection_error(self, movie_patch):
        with self.assertRaises(Exception) as example_error:
            mock_user_date = '1995-06-16'
            mock_calendar_date = CalendarDate.get_date_parts(mock_user_date)
            movie_api_response = API_Movie_Call.movie_call(mock_calendar_date)
            self.assertEqual(movie_api_response.connection_error, str(example_error))

if __name__ == '__main__':
    unittest.main()