import psycopg2
import os

# Get the connection
# create cursor from connection
#exeute query using cursor
from psycopg2 import OperationalError
try:

 connection =  psycopg2.connect(
      database="expense",
      host = "localhost",
      user="postgres",
      password=os.environ.get("POSTGRES_PWD"),
      port = "5433")

 cursor = connection.cursor()
 query = '''select * from grocery'''
 cursor.execute(query)
 print(cursor.fetchmany(size=2))
 cursor.close()
 connection.commit()
 connection.close()
except OperationalError:
    print("Unable to execute query")
except Exception as e:
    print("Error while connecting to db" + e)

print("Connection success")
