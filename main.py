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

conn.commit()  # saves the progress in the database

while True:
    print("\nMenu:")
    print("1. Add Column")
    print("2. Insert A Word")
    print("3. View All Data")
    print("4. Delete a column")

    cmd = int(input("Enter a command number: "))

    if cmd == 1:
        cname = input("Enter the name of the column: ")
        query = f"ALTER TABLE wordlist ADD `{cname}` TEXT"
        cursor.execute(query)
        print(f"Added a new column '{cname}' to table 'wordlist'.")
        conn.commit()

    elif cmd == 2:
        word = input("Enter the word you want to insert: ")
        cname = input("Please enter name of the column: ")

        if word and cname:
            try:
                query = f"INSERT INTO wordlist (`{cname}`) VALUES (%s)"
                cursor.execute(query, (word,))
                conn.commit()
                print(f"Inserted '{word}' into column '{cname}'.")
                
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                print("Please enter a valid column name!")

    elif cmd == 3:
        cursor.execute("SELECT * FROM wordlist")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif cmd == 4: 
        cname = input("Enter name of the column you want to delete: ")
        query = f"ALTER TABLE wordlist DROP COLUMN {cname}"
        try:
            if cname != "id":
                cursor.execute(query)
                print(f"Successfully deleted column: {cname}")
            else:
                print("You cannot delete the 'id' column!")
        except:
            print("Please enter a valid column name!")   


    else:
        print("Invalid command.")


