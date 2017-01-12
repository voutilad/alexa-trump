"""
Tests for Alexa Intents using Flask-Ask
"""
from dear_leader import alexa

def test_welcome():
    """
    Are we prompted to setup our skill on first welcome?
    """
    statement = alexa.welcome()
    assert "hey man" in statement._response['outputSpeech']['text']


