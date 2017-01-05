from __future__ import print_function
import os
import random
import twitter

TWITTER_CONSUMER_KEY=os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET=os.environ['TWITTER_CONSUMER_SECRET']

def get_random_tweet(session):
    """
    Grab token from session and get a tweet!
    """
    token = session['user']['accessToken'].split(',')
    key, secret = token[0], token[1]
    api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                      consumer_secret=TWITTER_CONSUMER_SECRET,
                      access_token_key=key, access_token_secret=secret)

    timeline = api.GetUserTimeline(screen_name='realDonaldTrump',
                                   include_rts=False,
                                   trim_user=True,
                                   exclude_replies=True,
                                   count=100)

    tweet = timeline[random.randint(0, len(timeline))]
    return tweet.text

def build_speechlet_response(output, card_title='Donald Trump said...',
                             reprompt_text='', card_type='Simple',
                             should_end_session=True):
    """
    Build the JSON speechlet response.
    """
    return {
        'version': '1.0',
        'sessionAttributes': {},
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': card_type,
                'title': card_title,
                'content': output
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': reprompt_text
                }
            },
            'shouldEndSession': should_end_session
        }
    }

def handle_session_end_request():
    """
    Thank the user and exit the skill.
    """
    card_title = "Session Ended"
    speech_output = "Thanks for trying Random Trump Tweets!"
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def build_tweet_response(session, prephase=None):
    """
    Build the response text for a Donald Trump tweet
    """
    if prephase is None:
        prephase = ''

    tweet = prephase + 'On Twitter, Donald Trump said: ' + \
            get_random_tweet(session)
    return build_speechlet_response(output=tweet,
                                    card_title='Random Trump Tweets',
                                    should_end_session=True)


def on_launch(launch_request, session):
    """
    Called during default launch with no specific user intent
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # right now we have one default intent, so whatever, man...
    return build_tweet_response(session,
                                prephase='Let me get a tweet for you...')

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # right now we have one default intent, so whatever, man...
    return build_tweet_response(session)


def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

def lambda_handler(event, context):
    """
    Main entry-point for the Lambda function.
    """
    ### Boilerplate from Amazon Lambda example
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    # Check if account is linked.
    if not event['session']['user'].has_key('accessToken'):
        return build_speechlet_response(
            "Please first link this skill to Twitter using the Alexa app.",
            card_type='LinkAccount', card_title='Link your Twitter account')


    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

if __name__ == '__main__':
    event = {
        'session': {
            'sessionId': 'fake-session',
            'application': {'applicationId': 'alexa-trump'},
            'new': True
        },
        'request': {
            'requestId': 'fake-request',
            'type': 'fake-type'
        }
    }
    lambda_handler(event, {})
    accessToken = os.environ['TWITTER_ACCESS_TOKEN'] + \
                  ',' + os.environ['TWITTER_ACCESS_SECRET']
    print(get_random_tweet({'user': {'accessToken': accessToken}}))
