"""
Test the interaction and statefulness
"""
from dear_leader import server
from dear_leader.settings import CLIENT_ID

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_if_get_to_index_redirects_to_github():
    """
    Make sure we send requests to our home/index page to Github.
    """
    response = client.get('/', follow_redirects=False)
    assert response is not None
    assert response.status_code == 302
    assert response.location == 'https://github.com/voutilad/alexa-trump'


def test_bad_client_id_results_in_403():
    """
    If we don't get the correct client-id, forbid going any further.
    """
    response = client.get('/oauth/authorize?client_id=abc&state=123')
    assert response is not None
    assert response.status_code == 403


def test_redirect_to_twitter_oauth():
    """
    Given valid client-id and a state, we should redirect to twitter
    """
    response = client.get('/oauth/authorize?client_id=' + CLIENT_ID +
                          '&state=123')
    assert response is not None
    assert response.status_code == 302
    assert 'https://api.twitter.com/oauth/authorize' in response.location
