from __future__ import print_function
import logging
from flask import Blueprint
from flask_ask import Ask, question, statement


ask_api = Blueprint('ask_api', __name__)
logger = logging.getLogger(ask_api.name)
ask = Ask(blueprint=ask_api)


@ask.launch
def welcome():
    return statement('hey man')
