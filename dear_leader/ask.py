from __future__ import print_function
import logging
from flask import Blueprint
from flask_ask import Ask, question


ask_api = Blueprint('ask_api', __name__)
ask_api.root
logger = logging.getLogger(ask_api.name)

ask = Ask(route=ask_api.rou)

@ask.launch
def welcome():
    return question('hey  man')
