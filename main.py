import argparse
import mysql.connector
import requests as r
import time 

#connects the code to the "mysql" db 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project_1"
)

cursor = conn.cursor()
#create the table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS wordlist (
               id INTEGER AUTO_INCREMENT PRIMARY KEY, 
               word TEXT
               );
               """) 

conn.commit()  # saves the progress in the database

#create commands with the help of the argparse module
parser = argparse.ArgumentParser(description="PYTHON FUZZING TOOL")
parser.add_argument("-c","--create", dest="create", help="creats a new column in the database", metavar="")
parser.add_argument("-a","--addwords", dest="add", help="adds a new word or list of words to the database", metavar="")
parser.add_argument("-col", "--column", dest="column", help="Specifies the column to add the word to", metavar="")
parser.add_argument("-s","--show", dest="show", help="shows the contents of the database", action="store_true")
parser.add_argument("-d","--delete", help="deletes an item from the database", metavar="")
parser.add_argument("-u", "--url", dest="url", help="specify the url you want to fuzz", metavar="")
parser.add_argument("-f", "--file", dest="file", help="specify a file with the urls you want to fuzz", metavar="")
parser.add_argument("-t","--time", dest="duration", help="specify timeout duration", type=int, metavar="")
args=parser.parse_args()

 #check if the creat command has been called
if args.create:
        cname = args.create
        #if yes take the value or string provided with it and create a new column with that name
        try:
            query = f"ALTER TABLE wordlist ADD `{cname}` TEXT"
            cursor.execute(query)
            print(f"Added a new column '{cname}' to table 'wordlist'.")
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

#add words to a column by using the -col to define the column
elif args.add :
    word = args.add
    cname=args.column
    if word and cname:
        try:
            query = f"INSERT INTO wordlist (`{cname}`) VALUES (%s)"
            cursor.execute(query, (word,))
            conn.commit()
            print(f"Inserted '{word}' into column '{cname}'.")
                
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Please enter a valid column name!")
#if -s is called show all words in the wordlist
elif args.show:
    cursor.execute("SELECT * FROM wordlist")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
#delete/drop the column
elif args.delete: 
    cname = args.delete
    query = f"ALTER TABLE wordlist DROP COLUMN {cname}"
    try:
        if cname != "id":
            cursor.execute(query)
            print(f"Successfully deleted column: {cname}")
        else:
            print("You cannot delete the 'id' column!")
    except:
        print("Please enter a valid column name!")   

#taking the url and replacing it with the words from the db

elif args.url:
    if args.file:
        url_file = open(args.file, "r")
        lines= url_file.read()
        newlines= lines.splitlines()
        for filewords in newlines:
            replace = args.url.replace("*", filewords)
            print(replace)
            try:
                duration= args.duration
                response = r.head(replace, allow_redirects=True, timeout=duration)
                if response.status_code == 200:
                    print("website exists")  # Website exists
                else:
                    print("website doesn't exist")  # Website doesn't exist
                time.sleep(1)
            except r.RequestException:
                    print("An error occurred!")

    else:            
        cursor.execute("select word from wordlist WHERE word IS NOT NULL")
        words = cursor.fetchall()
        for word in words:
            word =word[0]
            replace = args.url.replace("*", word)
            print(replace)
            try:
                duration= args.duration
                response = r.head(replace, allow_redirects=True, timeout=duration)
                if response.status_code == 200:
                    print("website exists")  # Website exists
                else:
                    print("website doesn't exist")  # Website doesn't exist
                time.sleep(1)
            except r.RequestException:
                    print("An error occurred!")

#none of the above
else:
    print("Invalid command.")
