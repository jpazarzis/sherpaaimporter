#!/usr/bin/python

import sys
from sherpaaimporter import importusers
'''
added fields should be added in the format: name:value
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

    importer = importusers.SherpaaImporter(config, added_fields)
    importer.process_file(csv_file)
