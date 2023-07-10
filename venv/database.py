import psycopg2

def get_connection():

    cnn = psycopg2.connect(
    host = "localhost",
    database = "technical_support",
    user = "postgres",
    password = "root"
)
    return cnn