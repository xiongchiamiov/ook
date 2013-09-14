'''ook-setup

Usage:
    ook setup
    ook setup (-h | --help)

Options:
    -h --help           Show this screen.
'''

import os

import envoy
from docopt import docopt

def runOrFail(command):
    result = envoy.run(command)
    if result.status_code != 0:
        exit(result.std_err)

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    
    home = os.environ['HOME']
    runOrFail('mkdir -p %s/.ook/cache' % home)
    runOrFail('mkdir -p %s/bin' % home)

