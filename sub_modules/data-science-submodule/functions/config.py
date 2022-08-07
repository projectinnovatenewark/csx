import os
from dotenv import load_dotenv
load_dotenv()

user = os.environ.get('POSTGRES_USER', 'pg user not found')
password = os.environ.get('POSTGRES_PASSWORD', 'pg password not found')
host = os.environ.get('POSTGRES_HOST', 'pg host not found')
database = os.environ.get('POSTGRES_DB', 'pg database not found')
port = os.environ.get('POSTGRES_PORT', 'pg port not found')
 
def get_connection():
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"