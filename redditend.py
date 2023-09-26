import praw
import random


reddit = praw.Reddit(
    client_id="pRelstLyzhnfoXMkTe0fTA",
    client_secret="UNx5xEb1inOdUxNkpatELWpTHiD1_w",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    username="Asrielthemonster3",
    password=">rv34ptrX9J:vEZ",
    check_for_async=False,
)

def getMemes():
  subreddit = reddit.subreddit("memes")
  post = subreddit.random()
  return post