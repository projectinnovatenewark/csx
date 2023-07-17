import psycopg2 


psycopg2.connect = user = 'postgres'
password = 'abcde12345'
host = 'localhost'
database = 'fitter'
port = '5432'

def get_connection():
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"