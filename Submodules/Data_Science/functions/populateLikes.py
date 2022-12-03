"""
programmatically creates likes and creates MORE likes for tweets of longer length.
This is so we can demo the linear relationship between tweet length and likes per tweet.
"""

#TIP: FOR DAY 2 - REMEMBER TO CREATE A LINEAR RELATIONSHIP BETWEEN THE LIKES AND NUMBER OF TWEETS

#TODO: Rename files to be snake case and variable names.

from executeQuery import execute_query
from queryRows import get_all_users
import random

tweet_query = "SELECT * FROM tweets;"

tweets = execute_query(tweet_query)
MAX_TWEET_LENGTH = 280

users = get_all_users()

#create at least 100 users

for tweet in tweets:
    tweet_obj = tweet._mapping
    # print(tweet_obj)
    tweet_length = len(tweet_obj['content'])
    existing_likes = set()
    existing_likes.add(tweet_obj['username'])
    for _ in range(20):
        # part over whole as tweet_length is somewhere between 0 and 280
        probability = tweet_length / MAX_TWEET_LENGTH
        #if tweet is 28 characters long, we want a 10% chance that it is liked per iteration
        like_or_not = random.random() < probability
        if like_or_not:
            id = tweet_obj['id']
            username = ""
            num_tries = 3
            while not username and num_tries:
                likee = users[random.randint(0, len(users) - 1)]['username']
                if likee not in existing_likes:
                    username = likee
                print(likee)
                num_tries -= 1
            #if we could not find a unique username to like this tweet, don't create a new like
            if not username:
                continue
            like_query_string = f"""INSERT INTO likes(username, tweet_id) VALUES
                                    ('{username}', 
                                    '{id}');"""
            existing_likes.add(username)
            execute_query(like_query_string)
