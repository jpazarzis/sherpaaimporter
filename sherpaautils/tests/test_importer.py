from unittest import TestCase
import os

from sherpaaimporter import importusers

dirname, filename = os.path.split(os.path.abspath(__file__))

VALID_CONFIG = os.path.join(dirname, 'config.ini')
USERS_FILENAME = os.path.join(dirname, 'fakeco_roster.csv')

class TestImporter(TestCase):
    def test_post(self):
        importer = importusers.SherpaaImporter(VALID_CONFIG, { 'employer' : 'FakeCo'})
        self.assertTrue(importer.add_user_url == 'http://127.0.0.1:5000/add_user')
        importer.process_file(USERS_FILENAME)

