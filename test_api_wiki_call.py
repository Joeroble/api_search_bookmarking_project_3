import unittest
from unittest import TestCase
from unittest.mock import patch

import API_Wiki_Call

class TestAPI_Wiki_call(TestCase):

    @patch('requests.Response.json')
    def test_api_wiki_call_data_returned(self, mock_wiki_json):
        mock_user_date = 'October 29'
        example_wiki_api_response = ['October 29', ['October 29'], [''], ['https://en.wikipedia.org/wiki/October_29']]
        mock_wiki_json.side_effect = [example_wiki_api_response]
        wiki_api_response = API_Wiki_Call.API_Wiki_Call(mock_user_date)
        self.assertTrue(mock_wiki_json, wiki_api_response)

    @patch('API_Wiki_Call.API_Wiki_Call', side_effect=Exception)
    def test_api_wiki_call_connection_error(self, wiki_patch):
        with self.assertRaises(Exception) as example_error:
            mock_user_date = 'October 29'
            wiki_api_response = API_Wiki_Call.API_Wiki_Call(mock_user_date)
            self.assertEqual(wiki_api_response.connection_error, str(example_error))

if __name__ == '__main__':
    unittest.main()