#!/usr/bin/python

import sys
from sherpaaimporter import sherpaahelper

'''
added fields should be added in the format: name:value

example of use:
importer.py config.ini fakeco_roster.csv employer:FakeCo

'''
if __name__ == '__main__':
    
    print sys.argv
    if sys.argv <3:
        print 'correct use: <configfile> <csvfile> <added fields>'
        sys.exit(0)

    config = sys.argv[1]
    csv_file = sys.argv[2]

    added_fields = { }

    for i in range(3, len(sys.argv)):
        key, value = sys.argv[i].split(":")
        added_fields[key] = value

    importer = sherpaahelper.SherpaaHelper(config, added_fields)
    importer.process_file(csv_file)
