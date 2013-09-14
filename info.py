'''ook-info

Usage:
    ook info [options] <script>
    ook info (-h | --help)

Options:
    -h --help           Show this screen.
    -a --all            List packages available from the remote library.
'''

import requests
from docopt import docopt

from config import config

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    scriptName = arguments['<script>']
    
    if arguments['--all']:
        print 'Available:'
        print '----------'
        libraryUrl = config.get('remote', 'url')
        response = requests.get('%s/scripts/%s' % (libraryUrl, scriptName))
        script = response.json()
        print 'Name: %s' % script['name']
        print 'Authors: %s' % ', '.join(script['admins'])

