from db_connection import *
import os
import psycopg2
import shutil
import datetime

try:
 connection = create_connection()
 cursor_variable = connection.cursor()

 with open("patients.txt", "r") as file:
    content = file.readlines()
    print(f"The data in the file :\n  {content}\n will be inserted in the database...........")
    for index, each_row in enumerate(content):
        if index == 0: #skips the header in the file
            continue
        #print(each_row)
        var1, var2, var3, var4, var5, var6, var7 = each_row.split(',')
        #print(f"{var1}, {var2}, {var3}, {var4},{var5}, {var6}, {var7}")
        query = f'''insert into public.patient_details (patient_id, first_name, last_name, email, gender, date_of_birth, next_appointment_date) values ({var1},'{var2}','{var3}','{var4}','{var5}',to_date('{var6}','MM/DD/YYYY'),to_date('{var7}', 'MM/DD/YYYY'))'''
        cursor_variable.execute(query)
    print("\n.......Data has been successfully inserted in the database table.............")
 connection.commit()
 connection.close()

except FileNotFoundError:
    print('The file could not be found.')
except ConnectionError:
    print("Error in Database connection.")
except Exception:
    print("Error ")

##### - creating the patient notification---------------------
try:
    connection = create_connection()
    cursor_variable = connection.cursor()
    query = "SELECT * FROM patient_details where next_appointment_date < current_date + interval '10 days' "
    cursor_variable.execute(query)
    result = cursor_variable.fetchall()
    for each_value in result:
        name = each_value[1].strip()
        appt_date = each_value[6]
        print(f"\n{name} - {appt_date}")
        filename = f"{name}.txt"
        #print(filename)
        f = open(f"./Notification/{filename}", "w")
        f.write(f" Hi {name},\n you have an upcoming appointment on {appt_date}.\n Please arrive on time.\n\n Thank you ")
        f.close()
    print("\n........Patients with recent appointment were sent notification...........")
    connection.close()
except Exception:
    print("Error ")