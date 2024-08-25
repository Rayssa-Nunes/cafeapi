import psycopg2
import os


def get_db_connection():
    conn = psycopg2.connect(
        host = "localhost",
        database = "cafeapi",
        user = os.environ['DB_USERNAME'],
        password = os.environ['DB_PASSWORD'])
    
    return conn

