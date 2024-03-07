import os
import psycopg2
import shutil
import datetime


def create_connection():
    pwd = os.environ.get("deepa_postgress_pwd")
    connection = psycopg2.connect(database="sample_db", host="localhost", user="postgres", password=pwd, port=5432)
    return connection
    print("Connection Successful")


connection = create_connection()
cursor_variable = connection.cursor()
with open ("patient_file.csv", "r") as file:
     #print(file.read())
     content = file.readlines()
     print(content)
     for each_row in content:
          print(each_row)
          var1,var2,var3,var4 = each_row.split(',')
          print(f"{var1},{var2},{var3},{var4}")
          query = f'''insert into patient (patient_id, patient_name, address, next_appointment) values ({var1},'{var2}','{var3}','{var4}')'''
          cursor_variable.execute(query)
connection.commit()
connection.close()
#except Exception:
 #   print("Error")
