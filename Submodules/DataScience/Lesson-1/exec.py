from sqlalchemy import create_engine
from config import get_connection
from sqlalchemy import create_engine, text

DB_CONNECTION_STRING = get_connection()

def execute_query(statement):

  DB_CONNECTION_STRING = get_connection()
  engine = create_engine(DB_CONNECTION_STRING, future=True)

  with engine.connect() as con:
      print("running query: ", statement)
      res = con.execute(text(statement))
      con.commit() # not needed in sqlalchemy>2.0
      return res