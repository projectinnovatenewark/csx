from sqlalchemy import create_engine
from config import get_connection
from sqlalchemy import create_engine, text

DB_CONNECTION_STRING = get_connection()

def execute_query(statement):
  """
  It takes a SQL statement as a string, connects to the database, and returns the results of the query
  
  :param statement: The SQL statement to execute
  :return: The result of the query.
  """
  DB_CONNECTION_STRING = get_connection()
  engine = create_engine(DB_CONNECTION_STRING, future=True)

  with engine.connect() as con:
      print("running query: ", statement)
      res = con.execute(text(statement))
      con.commit() # not needed in sqlalchemy>2.0
      return res