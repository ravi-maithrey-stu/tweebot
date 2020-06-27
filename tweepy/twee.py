import tweepy

auth = tweepy.OAuthHandler("$CLIENT_KEY", "$CLIENT_SECRET")
auth.set_access_token("$ACCESS_KEY", "$ACCESS_TOKEN")

api = tweepy.API(auth)

new_txt = open("new.txt", "r")
tweet = new_txt.readline()
api.update_status(tweet)
