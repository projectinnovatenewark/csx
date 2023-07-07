user = '<YOUR_POSTGRES_USER>'
password = '<YOUR_POSTGRES_PASSWORD>'
host = '<YOUR_POSTGRES_HOST>'
database = '<YOUR_POSTGRES_DB>'
port = '<YOUR_POSTGRES_PORT>'
 
def get_connection():
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"