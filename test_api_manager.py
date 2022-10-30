import unittest
from unittest import TestCase
from unittest.mock import patch

import API_Wiki_Call
import API_Movie_Call
import API_Nasa_Call
import API_Response

class Test_API_Manager(TestCase):

    @patch('API_Wiki_Call.API_Wiki_Call', return_value = API_Response.API_Response(data= ['https://en.wikipedia.org/wiki/October_29']))
    def test_api_wiki_call_response(self, mock_api_response):
        mock_user_date = 'October 30'
        expected_wiki_api_response = API_Response.API_Response(data=['https://en.wikipedia.org/wiki/October_29'])
        wiki_api_response = API_Wiki_Call.API_Wiki_Call(mock_user_date)
        self.assertEqual(expected_wiki_api_response.data, wiki_api_response.data)



    @patch('API_Nasa_Call.nasa_call', return_value = API_Response.API_Response(data= {
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
            'title':'Neutron Star Earth'}))
    def test_api_nasa_call_response(self, mock_api_response):
        mock_user_date = '1995-06-16'
        expected_nasa_api_response = API_Response.API_Response(data={
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
            'title':'Neutron Star Earth'})
        nasa_api_response = API_Nasa_Call.nasa_call(mock_user_date)
        self.assertEqual(expected_nasa_api_response.data, nasa_api_response.data)

    
#TODO movie_api_response_test

if __name__ == '__main__':
    unittest.main()