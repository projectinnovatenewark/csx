"""
The purpose of this file is for sending a request to randomuser api and then populate our db with some fake users

TODO: Populate files could be potentially combined?
"""

"""
File for sending a request to randomuser api and then populate our db with some fake users.
"""

import requests #TODO: pip3 install requests
from executeQuery import execute_query
from sqlalchemy import text
from config import *


results_number = int(input("Enter desired number of new users: "))
response = requests.get(f"https://randomuser.me/api/?results={results_number}")
res = response.json()

users = res["results"]
user_list = []

for user in users:
    username = user["login"]["username"]
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    phone = user["phone"]
    birthday = "2020-02-02"
    age = user["dob"]["age"]
    created_at = "CURRENT_TIMESTAMP"

    user_query_string = f"""INSERT INTO users (username, first_name, last_name, phone, birthday, age, created_at) VALUES
                        ('{username}', 
                        '{first_name}', 
                        '{last_name}', 
                        '{phone}', 
                        '{birthday}', 
                         {age}, 
                         {created_at});"""

    execute_query(user_query_string)

    #extra credit question: why are the created_at timestamps very similar but differnet by fractions of a second?
    