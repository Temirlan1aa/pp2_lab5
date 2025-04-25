import psycopg2 
import csv 
Connection = psycopg2.connect(
    dbname = "lab",
    user = "postgres",
    password = "temir2007",
    host = "localhost",
    port = "5432"
)
cur= Connection.cursor()
print("fpoaja")
def task1():
    name = input("username: ")
    phone = input("phone_number: ")
    cur.execute("SELECT * FROM phonebook")
    cur.execute("INSERT INTO phonebook (name,phone)  VALUES (%s , %s ) " , (name,phone) )
    Connection.commit()

def rename():
    name = input("username:")
    phone = input("phone_number:")
    cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (name, phone))

def filtr():
    number = int(input("write number 1-2:"))
    if number == 1:
        name=input()
        cur.execute("SELECT * FROM phonebook WHERE name LIKE  %s", ('%' + name + '%',))
        rows = cur.fetchall()
        for row in rows:
            print(row)

    elif number == 2:
        phone=input()
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE  %s", ('%' + phone+ '%',))
        rows = cur.fetchall()
        for row in rows:

        
            print(row)

    else:
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        for row in rows:
            print(row)

def delete():
    number = int(input("write number 1-2:"))
    if number == 1:
        name=input()
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name ,))
        Connection.commit()
    elif number == 2:
        phone= input()
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone ,))
        Connection.commit()

def alter():
    cur.execute("ALTER SEQUENCE phonebook_id_seq RESTART WITH 1")
    Connection.commit()




choice = int(input("plz number:"))
if choice == 1:
    task1()
elif choice == 2:
    rename()
elif choice == 3:
    filtr()
elif choice == 4:
    delete()
elif choice == 5:
    alter()
else:
    print("plz select number")