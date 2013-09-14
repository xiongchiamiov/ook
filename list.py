'''ook-list

Usage:
    ook list [options]
    ook list (-h | --help)

Options:
    -h --help           Show this screen.
    -a --all            List packages available from the remote.
'''

import requests
from docopt import docopt

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    
    if arguments['--all']:
        print 'Available:'
        print '----------'
        response = requests.get('http://localhost:8000/api/scripts/')
        for script in response.json():
            print script['name']

