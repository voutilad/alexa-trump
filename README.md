![alt the donald][Trump 108x108.png]
# Trump's Twitter
Alexa skill for hearing random Trump tweets!

Ask Alexa:
* `Alexa, open Trump's Twitter.`
* `Alexa, open Trump's Twitter and read a random tweet.`

Etc.

**Sample Audio**: [Alexa and Trump Sample.m4a](Alexa and Trump Sample.m4a)

## Lambda
This is the core skill logic to put in Amazon Lambda based on some boilerplate
from Amazon. It talks to Twitter via their API to fetch tweets and handles
using the Alexa SDK.

## Server
This is a Flask app for deployment to Heroku for brokering account linking
between Alexa and Twitter using OAuth. This is so stupid. Seriously. It's
just a proxy to facilitate OAuth.

Technically, you could merge both projects into one web app and host in one
location...but using Lambda & Heroku keeps it dirt cheap $$$.


# License!
The included source code is copyright Dave Voutila, 2017 and licensed under
the GPL v3.0. See LICENSE file for more details.

The Trump images are from: [Gage Skidmore](https://www.flickr.com/photos/22007612@N05/29273256122)
Attributed to: Gage Skidmore from Peoria, AZ, United States of America
And under CC BY-SA 2.0
