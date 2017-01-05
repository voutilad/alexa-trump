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
    """
    The Alexa app should call this, passing in 'state', 'client_id',
    'response_type', 'scope', and a 'redirect_uri'. We need 'state' and the
    generated oauth code. We don't use 'scope' at the moment.
    """
    state = request.args.get('state')
    client_id = request.args.get('client_id')
    redirect_uri = request.args.get('redirect_uri')

    if state and client_id:
        return twitter.authorize(
            callback=url_for('oauth_authorized', next=redirect_uri))
    else:
        return '<html><body>Hey, man. Are you using Alexa or not?</body></html>'


@app.route('/oauth-authorized')
def oauth_authorized():
    resp = twitter.authorized_response()
    if resp is None:
        return 'None'
    else:
        return str(resp)

if __name__ == "__main__":
    app.secret_key = os.environ['FLASK_SECRET_KEY']
    #app.debug = True
    app.run()
