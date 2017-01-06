# A basic Flask-based OAuth proxy

This is a [Flask](http://flask.pocoo.org)-based app for brokering OAuth 1.0a
authorization via Twitter.

Originally I came across an [example server](https://github.com/bignerdranch/alexa-account-linking-service)
from the folks at bignerdranch, but it:
1. Was Ruby-centric
2. Didn't explain some of the details of token handling

_Note: This is all about using Amazon's "implicit grant". See the
[Linking an Alexa User with a User in Your System](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/linking-an-alexa-user-with-a-user-in-your-system)
page on their documentation for details._

## Interesting things to Note!
I learned some stuff in the process of whipping this up using
[Flask](http://flask.pocoo.org) and
[Flask-OAuthlib](https://flask-oauthlib.readthedocs.io). Some of it makes me sad.

### The URL Fragment Gotcha
So Amazon _should_ generate a redirect url for you that you use after you get
the authorization from Twitter. The catch is that if you're using _implicit_
authorization, like in this project, you build the final version of the url a
bit differently than you'd probably expect. (Ok, yes, the docs are explicit
on this...but if you skim them and use common sense to fill in blanks you'll
be caught in this trap.)

Example given `redirect_url`:
```
https://pitangui.amazon.com/spa/skill/account-linking-status.html?vendorId=AAAAAAAAAAAAAA
```

You need to pass the previously given *state*, the new *token*, and a
*token_type* as part of this redirect url. Obvious first thought would be
something like:

```
https://pitangui.amazon.com/spa/skill/account-linking-status.html?vendorId=AAAAAAAAAAAAA&state=my_state&token=my_token&token_type=Bearer
```

_BUT NOOOOOOO..._ You need to use a [# (i.e. a url fragment identifier)](https://en.wikipedia.org/wiki/Fragment_identifier) instead of
adding more query parameters.

`(╯°□°)╯︵ ┻━┻`

### Twitter Token Gotcha
So Amazon wants you to return a single token value for implicit authorization
use cases. The type of token, in OAuth parlance, is a [bearer token](http://oauthlib.readthedocs.io/en/latest/oauth2/tokens/bearer.html).

This poses 2 Gotcha's in one!

1. You _must_ return a *token_type* parameter set to `"bearer"` even though
that is the __only__ option supported by the implicit auth method.
2. Twitter's tokens are really [OAuth1.0 Access Tokens](https://oauth.net/core/1.0a/#rfc.section.6.3.2) which have two parts to
them: a token and a secret.

So what do you give back to Amazon? UP TO YOU DUDE. You've got to serialize the
two-part *Access Token* into a single *Bearer Token* and then __make sure you
deserialize it in your Alexa skill code__.

## Helpful Libraries Used
* [Flask](http://flask.pocoo.org)
* [Flask-OAuthlib](https://flask-oauthlib.readthedocs.io)
* [gunicorn](http://gunicorn.org)

## Deploying to Heroku
Lastly, this project has some other files in place to help deploying to a
[Heroku dyno](https://www.heroku.com). Specifically the following files:
* [Profile](../Procfile) - tells Heroku how to launch the app using gunicorn
* [runtime.txt](../runtime.txt) - just specifies it's a python2.7 app
