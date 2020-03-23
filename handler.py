import os
import json
import tweepy

creds = json.loads(os.getenv("CREDS"))
# Authenticate to Twitter
auth = tweepy.OAuthHandler(creds["CONSUMER_KEY"], creds["CONSUMER_SECRET"])
auth.set_access_token(creds["ACCESS_TOKEN"], creds["ACCESS_TOKEN_SECRET"])

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


def hello(event, context):
    print("hi")
    api.update_status("We are alive.")


if __name__ == "__main__":
    hello('', '')