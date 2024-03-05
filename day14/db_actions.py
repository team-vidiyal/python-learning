import psycopg2
import os


def create_connection():
    try:
        password = os.environ.get("POSTGRES_PWD")
        connection = psycopg2.connect(
            database="expense",
            host="localhost",
            user="postgres",
            password=password,
            port="5433")
        return connection
    except Exception:
        print("connection error")
