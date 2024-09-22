
import mysql.connector 


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project_1"
)

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS wordlist (
               id INTEGER AUTO_INCREMENT PRIMARY KEY, 
               word TEXT
               );
               """) 

conn.commit() # saves the progress in Database

while True:
    print("\nMenu:")
    print("1. Add Column")
    print("2. View All Data")

    cmd = int(input("Enter a command number: "))

    if cmd == 1:
        cname = input("Enter name of column: ")
        c = conn.cursor()
        query = "ALTER TABLE wordlist ADD {} TEXT".format(cname)
        c.execute(query)
        print(f"Added a new column {cname} to table 'word list'.")
        conn.commit()

    if cmd == 2:
        c = conn.cursor()
        c.execute("""SELECT * FROM wordlist""")
        r = c.fetchall()
        for i in r:
            print(i)






