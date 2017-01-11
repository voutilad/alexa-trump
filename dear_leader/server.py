"""
Flask OAuth Server for proxying Amazon Alexa to Twitter.
"""
from __future__ import print_function
import os
from flask import Flask, redirect
from flask_ask import Ask, statement, question, session
from dear_leader.oath import oauth_api

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
app.register_blueprint(oauth_api, url_prefix='/oauth')


@app.route('/')
def home():
    """
    Redirect to our project page for now.
    :return: redirect to github
    """
    return redirect('https://github.com/voutilad/alexa-trump')


if __name__ == "__main__":
    import logging
    import sys
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    app.debug = True
    app.run(host='0.0.0.0')
