from __future__ import print_function
import logging
from flask import Blueprint, redirect


web_api = Blueprint('web_api', __name__)
logger = logging.getLogger(web_api.name)


@web_api.route('/')
def home():
    """
    Redirect to our project page for now.
    :return: redirect to github
    """
    return redirect('https://github.com/voutilad/alexa-trump')