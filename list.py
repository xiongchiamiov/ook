'''ook-list

Usage:
    ook list [options]
    ook list (-h | --help)

Options:
    -h --help           Show this screen.
    -a --all            List packages available from the remote library.
'''

import json
import os

import requests
from docopt import docopt

from config import config

installedScripts = json.load(open('%s/.ook/library' % os.environ['HOME']))

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    
    if arguments['--all']:
        print 'Available:'
        print '----------'
        libraryUrl = config.get('remote', 'url')
        response = requests.get('%s/scripts/' % libraryUrl)
        for script in response.json():
            print script

