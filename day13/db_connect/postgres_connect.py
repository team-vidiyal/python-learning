import psycopg2

# Get the connection
# create cursor from connection
#exeute query using cursor
from psycopg2 import OperationalError

try:
 connection =  psycopg2.connect(
      database="expense",
      host = "localhost",
      user="postgres",
      password="test",
      port = "5433")

 cursor = connection.cursor()
 query = '''INSERT INTO grocery(item_id, item_name, price) VALUES (102, Orange, 4);'''
 cursor.execute(query)
 connection.commit()
 connection.close()
except OperationalError:
    print("Unable to execute query")
except Exception:
    print("Error while connecting to db")

print("Connection success")
