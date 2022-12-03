"""
The purposes of this file is to ccreate rows for *already existing* tables and columns.
"""
from executeQuery import execute_query
import datetime

#IMPORTANT: is this how we want the values to be represented and fed into python? maybe interact with terminal?
#TODO: DONE Myko -> I will implement an option for the user to assign these values from the terminal.  

username = input("Enter a username: ")
first_name = input("Enter a first name: ")
last_name = input("Please enter a last name: ")
phone = input("Please enter a phone number: ")
birthday = input("Please enter a birthday in the following format: YYYY-MM-DD")
age = int(input("Please enter the age of the user in years: "))

created_at = "CURRENT_TIMESTAMP" # 2020-07-28 20:12:12


user_query_string = f"""INSERT INTO users (username, first_name, last_name, phone, birthday, age, created_at) VALUES
                        ('{username}', 
                        '{first_name}', 
                        '{last_name}', 
                        '{phone}', 
                        '{birthday}', 
                         {age}, 
                         {created_at});"""

execute_query(user_query_string)