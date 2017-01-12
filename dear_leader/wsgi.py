"""
Entry-point for WSGI applications
"""
import logging
import os
import sys
from dear_leader.server import create_app


application = create_app()

if 'FLASK_DEBUG' in os.environ:
    application.debug = True

if application.debug:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO

logging.basicConfig(stream=sys.stdout, level=log_level)


