'''ook-install

Usage:
    ook install [options] <script>
    ook install (-h | --help)

Options:
    -h --help           Show this screen.
'''

import json
import os

import requests
from docopt import docopt

from config import config
from list import installedScripts

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    scriptName = arguments['<script>']
    if scriptName in installedScripts:
        exit('%s already installed.' % scriptName)
    
    libraryUrl = config.get('remote', 'url')
    response = requests.get('%s/scripts/%s' % (libraryUrl, scriptName))
    script = response.json()
    
    # TODO: Actually install something...
    
    installedScripts[scriptName] = {
        'version': script['version'],
    }
    json.dump(installedScripts,
              open('%s/.ook/library' % os.environ['HOME'], 'w'),
              indent=4)

