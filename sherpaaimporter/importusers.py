import csv
import json
import requests
import ConfigParser

MAIN_INI_SECTION='sherpaa_importer_settings'

class SherpaaImporter(object):
    def __init__(self, config_file, additional_fields = None):
        '''
        Creates a Sherpaa importer file 
        @config_file: an ini file containing the necessary settings
        @additional_fields: dictionary with additional fields
        '''
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        self.add_user_url =  config.get(MAIN_INI_SECTION, 'add_user_url')
        self.all_fields = config.get(MAIN_INI_SECTION, 'all_field_names').split(' ')
        self.fields_to_skip = config.get(MAIN_INI_SECTION, 'fields_to_skip').split(' ')
        self.additional_fields = additional_fields

    def process_file(self, filename):
        with open(filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, self.all_fields)
            data = json.loads(json.dumps([r for i, r in enumerate(csv_reader) if i >0  ]))

            if self.additional_fields is not None:
                map(lambda user: user.update(self.additional_fields)  ,data)
        
            map(lambda user: remove_fields(user, self.fields_to_skip)  ,data)
            map(self.post_to_server, data)

    def post_to_server(self, user_data):
        headers = {'Content-Type': 'application/json'}

        age = 2014 - int(user_data['birthdate'][6:])
        if age >= 18:
            r = requests.post(self.add_user_url, data=json.dumps(user_data), headers=headers)


def remove_fields(user, fields_to_skip):
    for field in fields_to_skip:
        if field in user:
            del user[field]
