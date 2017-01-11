"""
Entry-point for WSGI applications
"""
import logging
import os
import sys
from dear_leader.server import app


if 'FLASK_DEBUG' in os.environ:
    app.debug = True

if app.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO

logging.basicConfig(stream=sys.stdout, level=log_level)
application = app

