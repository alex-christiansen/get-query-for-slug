### Get Query for Slug
**Description**

This simple script allows a user to find the slug associated with a given query ID. It is an alternative to looking up slugs via Looker System Activity 

**Requirements**

Python 3.11.6, [looker-sdk](https://pypi.org/project/looker-sdk/), argparse, urlparse

**Usage**

You'll need to set up an .ini file in order to authenticate into the Looker SDK. The repo has a sample .ini file (looker-example.ini). Make a copy of looker-example.ini called looker.ini with information from your Looker instance (url, client_id, client_secret). 

Once you set up your .ini file, you'll be ready to use the script, just run `python3 get_slug_for_query.py {query_id}`. The script currently only allows users to input one query ID but it could be easily altered to accept multiple IDs or a CSV of IDs.  
