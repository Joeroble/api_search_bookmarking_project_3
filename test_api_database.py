import sqlite3
import unittest
from unittest import TestCase
from unittest.mock import patch

import API_Database

class TestAPI_Database(TestCase):

    test_api_db_url = 'test_ap.db'

    def setUp(self):
        API_Database.ap_db_url = self.test_api_db_url

        with sqlite3.connect(self.test_api_db_url) as conn:
            conn.execute('DELETE from API')
        conn.close()


    def test_api_database():
        pass
