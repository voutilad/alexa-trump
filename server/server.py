from __future__ import print_function
import os
from flask import Flask, url_for, request
from flask_oauthlib.client import OAuth
from flask_oauthlib.contrib.apps import twitter

app = Flask(__name__)
oauth = OAuth(app)
twitter = oauth.remote_app(
    'twitter',
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize'
)

@app.route('/authorize')
def authorize():
    return twitter.authorize(
        callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
def oauth_authorized():
    resp = twitter.authorized_response()
    if resp is None:
        return 'None'
    else:
        return str(resp)

if __name__ == "__main__":
    app.secret_key = os.environ['FLASK_SECRET_KEY']
    app.run()
