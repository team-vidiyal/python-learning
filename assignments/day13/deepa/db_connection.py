import os
import psycopg2

def create_connection():
    pwd = os.environ.get("deepa_postgress_pwd")
    connection = psycopg2.connect(database="sample_db", host="localhost", user="postgres", password=pwd, port=5432)
    return connection


create_connection()
print("Connection Successful")