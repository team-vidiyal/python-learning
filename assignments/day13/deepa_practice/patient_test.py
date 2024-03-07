import os
import psycopg2
import shutil
import datetime


def create_connection():
    pwd = os.environ.get("deepa_postgress_pwd")
    connection = psycopg2.connect(database="sample_db", host="localhost", user="postgres", password=pwd, port=5432)
    return connection
    # print("Connection Successful")


try:
    connection = create_connection()
    cursor_variable = connection.cursor()
    query = "SELECT * FROM public.patient where next_appointment < current_date + interval '10 days' "
    cursor_variable.execute(query)
    result = cursor_variable.fetchall()
    print(result)
    ### print(type(result))
    for each_value in result:
        name = each_value[1].strip()
        appt_date = each_value[3]
        print(f"{name} - {appt_date}")
        filename = f"{name}.txt"
        print(filename)
        f = open(f"./text_notification/{filename}", "w")
        f.write(f"Hi {name},\n you have an upcoming appointment on {appt_date}.\n Please arrive on time.\n\n Thank you ")
        f.close()
    connection.close()



except Exception:
    print("Error in DB connection")
