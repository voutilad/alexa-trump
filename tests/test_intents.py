"""
Tests for Alexa Intents using Flask-Ask
"""
from dear_leader import ask

def test_welcome():
    """
    Are we prompted to setup our skill on first welcome?
    """
    question = ask.welcome()
    assert question is not None
    assert question

