import unittest
from unittest import TestCase
from unittest.mock import patch

import API_Nasa_Call

class TestAPI_Nasa_call(TestCase):

    @patch('requests.Response.json')
    def test_api_wiki_call_data_returned(self, mock_nasa_json):
        mock_user_date = '1995-06-16'
        
        example_nasa_api_response = {
                'date': '1995-06-16',
                'explanation': "Today's Picture:    Explanation:  If the Earth could somehow "
                                'be transformed to the ultra-high density of a neutron star , '
                                'it might appear as it does in the above computer generated '
                                'figure. Due to the very strong gravitational field, the '
                                'neutron star distorts light from the background sky greatly. '
                                'If you look closely, two images of the constellation Orion '
                                'are visible. The gravity of this particular neutron star is '
                                'so great that no part of the neutron star is blocked from '
                                'view - light is pulled around by gravity even from the back '
                                'of the neutron star.   We keep an  archive file.  Astronomy '
                                'Picture of the Day is brought to you by  Robert Nemiroff and  '
                                'Jerry Bonnell . Original material on this page is copyrighted '
                                'to Robert Nemiroff and Jerry Bonnell.',
                'hdurl': 'https://apod.nasa.gov/apod/image/e_lens.gif',
                'media_type': 'image',
                'service_version': 'v1',
                'title': 'Neutron Star Earth',
                'url': 'https://apod.nasa.gov/apod/image/e_lens.gif'}

        expected_nasa_api_response_data = {
            'image':'https://apod.nasa.gov/apod/image/e_lens.gif',
            'desc':"Today's Picture:    Explanation:  If the Earth could somehow "
                                'be transformed to the ultra-high density of a neutron star , '
                                'it might appear as it does in the above computer generated '
                                'figure. Due to the very strong gravitational field, the '
                                'neutron star distorts light from the background sky greatly. '
                                'If you look closely, two images of the constellation Orion '
                                'are visible. The gravity of this particular neutron star is '
                                'so great that no part of the neutron star is blocked from '
                                'view - light is pulled around by gravity even from the back '
                                'of the neutron star.   We keep an  archive file.  Astronomy '
                                'Picture of the Day is brought to you by  Robert Nemiroff and  '
                                'Jerry Bonnell . Original material on this page is copyrighted '
                                'to Robert Nemiroff and Jerry Bonnell.',
            'title':'Neutron Star Earth'
            }
        mock_nasa_json.side_effect = [example_nasa_api_response]
        nasa_api_response = API_Nasa_Call.nasa_call(mock_user_date)
        self.assertEqual(expected_nasa_api_response_data, nasa_api_response.data)


    @patch('API_Nasa_Call.nasa_call', side_effect=Exception)
    def test_api_nasa_call_connection_error(self, nasa_patch):
        with self.assertRaises(Exception) as example_error:
            mock_user_date = '1995-06-16'
            nasa_api_response = API_Nasa_Call.nasa_call(mock_user_date)
            self.assertEqual(nasa_api_response.connection_error, str(example_error))

if __name__ == '__main__':
    unittest.main()