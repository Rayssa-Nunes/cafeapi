import psycopg2
import os

connection = psycopg2.connect(
    dbname = 'cafeapi',
    user = os.environ['DB_USERNAME'],
    password = os.environ['DB_PASSWORD'],
    host = "localhost"
)

with open('schema.sql') as f:
    with connection.cursor() as cursor:
        cursor.execute(f.read())
        
connection.commit()
connection.close()
