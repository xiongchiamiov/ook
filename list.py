'''ook-list

Usage:
    ook list [options]
    ook list (-h | --help)

Options:
    -h --help           Show this screen.
    -a --all            List packages available from the remote library.
'''

import requests
from docopt import docopt

from config import config

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    
    if arguments['--all']:
        print 'Available:'
        print '----------'
        libraryUrl = config.get('remote', 'url')
        response = requests.get('%s/scripts/' % libraryUrl)
        for script in response.json():
            print script

