import praw
reddit = praw.Reddit(client_id = "$CLIENT_ID", client_secret = "$CLIENT_SECRET", user_agent = "$USER_AGENT")#creting an instance of the api
new_posts = reddit.subreddit("ComedyNecrophilia").new(limit = 1)#selecting top 10 posts when sorted by new
new_txt = open("new.txt", "w")
for post in new_posts:#iterating and printing through them
    new_txt.writelines(str(post.title))
new_txt.close()
