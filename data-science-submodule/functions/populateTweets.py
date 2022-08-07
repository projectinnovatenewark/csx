"""
The purpose of this file is for sending a request to randomtweet api and then populate our db with some fake tweets.
"""

from executeQuery import execute_query
from sqlalchemy import text
from config import *
import random


lorem_ipsum =   ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 
                "Aenean rutrum dui sit amet tortor luctus, in congue felis auctor.", 
                "Curabitur congue velit nec commodo consequat.",
                "Quisque sit amet mauris vitae ligula condimentum laoreet."]

results_number = int(input("Enter desired number of new tweets: "))

for i in range(results_number):

    random_tweet_length = random.randint(1, 3)

    users_query =   """
                    SELECT username FROM users;
                    """

    users = execute_query(users_query)

    users_list = []

    for user in users:
        users_list.append(str(user)[2:-3])

    random_user_index = random.randint(0, len(users_list) - 1)

    lucky_user = users_list[random_user_index]

    username = lucky_user
    content = " ".join(lorem_ipsum[:random_tweet_length])
    created_at = "CURRENT_TIMESTAMP"

    tweet_query_string = f"""INSERT INTO tweets(username, content, created_at) VALUES
                        ('{username}', 
                        '{content}', 
                         {created_at});"""

    execute_query(tweet_query_string)


