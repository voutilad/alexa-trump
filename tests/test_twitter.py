"""
Tests for interacting with Twitter
"""
import os
from alexa import trump

ACCESS_TOKEN_KEY = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_SECRET']

ACCESS_TOKEN = ACCESS_TOKEN_KEY + "," + ACCESS_TOKEN_SECRET
FAKE_SESSION = { "user": { "accessToken": ACCESS_TOKEN } }


def test_if_we_can_get_a_tweet():
    """
    Test if we can hit Twitter's timeline api and grab a tweet.
    """
    text = trump.get_random_tweet(FAKE_SESSION)
    assert text is not None
    assert len(text) > 0

def test_can_build_speech_response_from_tweet():
    """
    Test that we can properly build a response that contains expected
    text and card details.
    """
    response = trump.build_tweet_response(FAKE_SESSION)
    assert response is not None
    assert response['response']['outputSpeech']['text'] is not None
