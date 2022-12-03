"""
Have a file for the migration stuff (the CREATE TABLE IF NOT EXISTS …etc  commands) and call it schema.py
Add a “Likes” table to the contents of the original “schema” file, but put it in a new file.
"""

from executeQuery import execute_query

create_users_table = """CREATE TABLE IF NOT EXISTS users(
                            username varchar(100) primary key, 
                            first_name varchar(100), 
                            last_name varchar(100), 
                            phone varchar(100), 
                            birthday date, 
                            age int, 
                            created_at timestamp)"""

execute_query(create_users_table)

create_tweets_table = """CREATE TABLE IF NOT EXISTS tweets(
                            id serial not null primary key,
                            username varchar(100),
                            content varchar(280),
                            created_at timestamp,
                            FOREIGN KEY (username) REFERENCES users(username))"""

execute_query(create_tweets_table)

create_likes_table = """CREATE TABLE IF NOT EXISTS likes(
                            username varchar(100),
                            tweet_id serial not null,
                            FOREIGN KEY (username) REFERENCES users(username),
                            FOREIGN KEY (tweet_id) REFERENCES tweets(id),
                            PRIMARY KEY(tweet_id, username))"""  

execute_query(create_likes_table)

#Will thet tweet_id be necessary with serial increment

#TODO: Implement constraints