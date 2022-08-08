"""
Simple file for querying all the rows on those tables.
"""
from exec import execute_query

def get_all_users():
    users_query =   """
                    SELECT username FROM users;
                    """

    users = execute_query(users_query)
    return [user._mapping for user in users]
