from unittest import TestCase
import os

from sherpaautils import sherpaahelper

dirname, filename = os.path.split(os.path.abspath(__file__))

VALID_CONFIG = os.path.join(dirname, 'config.ini')
USERS_FILENAME = os.path.join(dirname, 'fakeco_roster.csv')
USERS_WITH_DEPENDENCIES_FILENAME = os.path.join(dirname, 'roster_with_dependets.csv')

EXPECTED_DEPENDS= ['Vluffernutter Uruguay', 'Lysenko,Nellie']
EXPECTED_EMPLOYEES= ['Wachowski Jenkins','Uvula Plato', 'Atkins Leonard']

EXPECTED_USERS = '''<regular user: Jenkins Wachowski -- employee at FakeCo; allowed issuetypes: ['sick', 'hurt', 'mental', 'insurance']>
<regular user: Plato Uvula -- employee at FakeCo; allowed issuetypes: ['sick', 'hurt', 'mental', 'insurance']>'''

class TestImporter(TestCase):
    def test_post(self):
        '''Posting '''
        importer = sherpaahelper.SherpaaHelper(VALID_CONFIG, { 'employer' : 'FakeCo'})
        importer.reset()
        self.assertTrue(importer.add_user_url == 'http://127.0.0.1:5000/add_user')
        importer.process_file(USERS_FILENAME)
        size = importer.size()
        self.assertEqual(size, 2)

    def test_reset(self):
        '''Reseting'''
        importer = sherpaahelper.SherpaaHelper(VALID_CONFIG, { 'employer' : 'FakeCo'})
        count = importer.reset()
        self.assertEqual(count, 0)

    def test_size(self):
        '''Get Size'''
        importer = sherpaahelper.SherpaaHelper(VALID_CONFIG, { 'employer' : 'FakeCo'})
        importer.reset()
        size = importer.size()
        self.assertEqual(size, 0)

    def test_list_users(self):
        '''List Users'''
        importer = sherpaahelper.SherpaaHelper(VALID_CONFIG, { 'employer' : 'FakeCo'})
        importer.reset()
        importer.process_file(USERS_FILENAME)
        size = importer.size()
        self.assertEqual(size, 2)
        self.assertEqual(importer.get_all_users().strip(), EXPECTED_USERS)


    def test_dependents(self):
        '''Test Depends'''
        importer = sherpaahelper.SherpaaHelper(VALID_CONFIG, { 'employer' : 'FakeCo'})
        importer.reset()
        importer.process_file(USERS_WITH_DEPENDENCIES_FILENAME)
        size = importer.size()
        self.assertEqual(size, 5)
        self.assertEqual(importer.count_dependents(), 2)

        
        


