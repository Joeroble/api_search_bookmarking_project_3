import unittest
from unittest import TestCase
from unittest.mock import patch

import API_Wiki_Call

class TestAPI_Wiki_call(TestCase):


    """Tests the api call is handling the data returned from the api, saving and returning it correctly."""
    @patch('requests.Response.json')
    def test_api_wiki_call_data_returned(self, mock_wiki_json):
        mock_user_date = 'October 29'
        example_wiki_api_response = ['October 29', ['October 29'], [''], ['https://en.wikipedia.org/wiki/October_29']]
        expected_wiki_api_response_data = ['https://en.wikipedia.org/wiki/October_29']
        mock_wiki_json.side_effect = [example_wiki_api_response]
        wiki_api_response = API_Wiki_Call.API_Wiki_Call(mock_user_date)
        self.assertEqual(expected_wiki_api_response_data, wiki_api_response.data)


    """Tests the api call is handling an erronous call, and saving it in user_error correctly."""
    @patch('requests.Response.json')
    def test_api_wiki_call_user_error(self, mock_wiki_jason):
        mock_user_error = 'Error with the date provided by user, please ensure date is not in the future.'
        mock_erronous_api_call = 'completegibberishtogetusererror'
        example_wiki_api_response = [mock_erronous_api_call, [],[],[]]
        mock_wiki_jason.side_effect = [example_wiki_api_response]
        wiki_api_response = API_Wiki_Call.API_Wiki_Call(mock_user_error)
        self.assertEqual(mock_user_error, wiki_api_response.user_error)


    "Tests that the api call will handle an exception and return the error saved in the ?_api_response.connection_error"
    @patch('API_Wiki_Call.API_Wiki_Call', side_effect=Exception)
    def test_api_wiki_call_connection_error(self, wiki_patch):
        with self.assertRaises(Exception) as example_error:
            mock_user_date = 'October 29'
            wiki_api_response = API_Wiki_Call.API_Wiki_Call(mock_user_date)
            self.assertEqual(wiki_api_response.connection_error, str(example_error))

if __name__ == '__main__':
    unittest.main()