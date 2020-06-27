import tweepy

auth = tweepy.OAuthHandler("mFOnhD11W4lPGUb9V7JgA8ZEG", "GVVCihE4u3hGAA6eyq3XNSbEl0YBfUFUCab5Ewl7qmQznijjoQ")
auth.set_access_token("1276845470686445568-eEiTJbbWZhAJBq5y4fCQoBfnTDXqDE", "K5UxTzHj0qu758aqlsLOID4iEAXbAcNj7EixvjtAsFPOr")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)