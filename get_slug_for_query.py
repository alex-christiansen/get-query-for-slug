import looker_sdk
import sys
from urllib.parse import urlparse
from looker_sdk import models40 as models

# log into the looker sdk
sdk = looker_sdk.init40("demo.ini")

# grab the query id 
query_id = sys.argv[1]

# get query
response = sdk.query(query_id=str(query_id))

# parse the share url 
url = urlparse(response.share_url)

# extract slug
slug = url.path.split("/")[2]

# print info
# validate 
response = sdk.query_for_slug(slug=slug)
if response.id == query_id:
    print("validation successful")
    print(f"""The slug for query id {query_id} is {slug}""")
else:
    print("error, try new query id or go to system activity link: ")


