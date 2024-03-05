from db_actions import *


# [   insert into grocery values (111, 'Apple', 20), insert into grocery values (111, 'Apple', 20), insert into grocery values (111, 'Apple', 20), ]
def insert_from_file():
    conn = create_connection()
    cursor = conn.cursor()
    with open("./queries.txt", "r") as file:
        queries = file.read().split(";")
        for query in queries:
            if query.strip():
                cursor.execute(query)

    conn.commit()
    conn.close()


insert_from_file()
