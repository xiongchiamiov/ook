'''ook-config

Usage:
    ook config [options]
    ook config (-h | --help)

Options:
    -h --help           Show this screen.
'''

import os
from ConfigParser import SafeConfigParser

from docopt import docopt

config = SafeConfigParser()
config.read('%s/.ook/config' % os.environ['HOME'])

def run(argv):
    arguments = docopt(__doc__, argv=argv)

