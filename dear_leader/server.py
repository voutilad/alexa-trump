"""
Flask OAuth Server for proxying Amazon Alexa to Twitter.
"""
from __future__ import print_function
import os
from flask import Flask
from dear_leader.default_web import web_api
from dear_leader.oath import oauth_api
from dear_leader.alexa import ask_api


def create_app(config_filename=None):
    """
    Application factory function
    :param config_filename: filename of a python file with the configs
    :return: new Flask application instance
    """
    app = Flask(__name__)
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        app.secret_key = os.environ['FLASK_SECRET_KEY']

    app.register_blueprint(oauth_api, url_prefix='/oauth')
    app.register_blueprint(ask_api, url_prefix='/ask')
    app.register_blueprint(web_api, url_prefix='/')
    return app


if __name__ == "__main__":
    import logging
    import sys
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    app = create_app()
    app.debug = True
    app.run(host='0.0.0.0')
