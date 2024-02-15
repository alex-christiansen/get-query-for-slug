### Get Query for Slug
**Description**

This simple script allows a user to find the slug associated with a given query ID. It is an alternative to looking up slugs via Looker System Activity 

**Requirements**

Python 3.11.6
[looker-sdk](https://pypi.org/project/looker-sdk/), argparse, urlparse

**Usage**

You'll need to set up an .ini file in order to authenticate into the Looker SDK. The repo has a sample .ini file (looker-example.ini). Make a copy of looker-example.ini called looker.ini with information from your Looker instance (url, client_id, client_secret). 

Change the 
