#!/usr/bin/python

import os
os.environ['PYTHON_EGG_CACHE'] = '/var/www/lovenotes/python-eggs' 

activate_this = '/var/www/lovenotes/lovenotes/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/lovenotes')
sys.path.append('/var/www/lovenotes')

from lovenotes import app as application
