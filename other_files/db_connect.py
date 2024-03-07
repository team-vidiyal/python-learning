import os
import psycopg2
import shutil

try :
    pwd = os.environ.get("deepa_postgress_pwd")
    connection = psycopg2.connect(database="sample_db", host="localhost", user="postgres", password=pwd, port=5432)
    print("Connection Successful")

    cursor_variable = connection.cursor()
    ##INSERT INTO public."Grocery"("Item_Id", "Item_name", "Price") VALUES(101, 'p', 100);
    ##query = '''INSERT INTO public."Grocery"("Item_Id", "Item_name", "Price") VALUES(104, 'p4', 100);'''
    query = '''INSERT INTO Grocery(Item_Id, Item_name, Price) VALUES(107, 'p7', 100);'''
    cursor_variable.execute(query)
    connection.commit()
    connection.close()

except Exception:
   print("Error in DB connection")


