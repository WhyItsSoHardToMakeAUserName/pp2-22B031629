#!/usr/bin/python
import psycopg
import csv
check = True
conn = psycopg.connect("dbname=phones user=postgres password=s09112001")
cur = conn.cursor()
conn.autocommit = True
cur.execute("""CREATE TABLE IF NOT EXISTS phonebook 
            (name TEXT,
            phone TEXT
            )""") 
while check:
    print(
        "[0] to exit\n[1] to add phone\n[2] to update phone\n[3] to delete phone\n[4] print data\n[5] add csv file")
    n = int(input())
    if n == 0:
        check = False
    if n == 1:
        print("write name:")
        name = input()
        print("write phone:")
        phone = input()
        cur.execute(f"INSERT INTO phonebook (name, phone) VALUES ('{name}', '{phone}')")

    if n == 2:
        print("write the user name which you want to update:")
        name = input()
        print("write the user phone which you want to update:")
        phone = input()
        print("write the new user name which you want to update:")
        new_name = input()
        print("write the new phone which you want to update:")
        new_phone = input()
        cur.execute(f"""UPDATE phonebook 
                        SET name = '{new_name}', phone = '{new_phone}'
                        WHERE name = '{name}' AND phone = '{phone}'""")
    if n == 3:
        print("write the user name which you want to delete:")
        name = input()
        print("write the user phone which you want to delete:")
        phone = input()
        cur.execute(f"DELETE FROM phonebook where ('{name}', '{phone}')")
    if n == 4:
        print("inser 0 to print not sorted\ninsert 1 to sort by name")
        a = int(input())
        if a == 0:
            cur.execute("select * from phonebook")
            data = cur.fetchall()
        if a == 1:
            cur.execute("select * from phonebook order by name")
            data = cur.fetchall()
        for i in data:
            print(i)
    if n == 5:
        with open('phone_data.csv') as file:
            reader = csv.reader(file, delimiter=',')
            for i in reader:
                name = i[0]
                phone = i[1]
                cur.execute(f"INSERT INTO phonebook (name, phone) VALUES ('{name}', '{phone}')")
    conn.commit()