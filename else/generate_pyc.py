#[generate_pyc.py]

import imp
import sys

from wsgiref.simple_server import make_server

from code import application

httpd = make_server('', 8000, application)
print('servi.......')

httpd.serve_forever()