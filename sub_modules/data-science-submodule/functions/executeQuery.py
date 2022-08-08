from sqlalchemy.sql.functions import user
from sqlalchemy import create_engine
from config import get_connection

"""
This file is meant to be for the purposes of executing a single query. Can be modified by the student to handle multiple queries for EC. 
"""

DB_CONNECTION_STRING = get_connection()

def execute_query(statement):
    """
    It takes a SQL statement as a string, connects to the database, sends and returns the results of the query
    
    :param statement: The SQL statement to execute
    :return: The result of the query.
    """
    DB_CONNECTION_STRING = get_connection()
    engine = create_engine(DB_CONNECTION_STRING)

    with engine.connect() as con:
        print("running command: ", statement)
        return con.execute(statement)

print(DB_CONNECTION_STRING)