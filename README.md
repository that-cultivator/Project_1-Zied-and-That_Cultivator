USAGE:


This is a beginner-level directory brute forcing command-line tool, it can save words in an sql database and use those words to feed the tool as completion for the url (the same could be done by feeding the tool a txt file containing a wordlist as the sql part was for mere learning practices).

Commands:


-c OR  --create : creates a new column in the sql database 
Example: python main.py -c “newcolumn”

As shown in the example above we run our python file just as we would for any other python file except we add the -command which is -c in this case, -c tells the program to create a new column and call it as it can be seen above: “newcolumn”.


-col OR --column : the -col command is used alongside the -a or --add command to specify which column we would like to add new words to.

-a OR --add: this command adds a new word or words to the column specified with the -col command.

-s AND -d: the -s command is used to view the column which we have our words saved up in, and the -d command deletes the column we specify in case we created one accidently.

-u OR --url: we use this command to specify the url we would like to brute-force.

For example: python main.py -u https://www.example.com/*

Note that star sign at the end there {*}, this is what the tool will replace with the words you saved to check if a website has some hidden directory.

Let’s say we saved 4 words inside the file wordlist or the database (admin, login, admin-login, admin-panel).

The code will run with the above given url and outputs for us 4 results:

https://www.example.com/admin 
website exists!
https://www.example.com/login
website exists!
https://www.example.com/admin-login
website exists! 
https://www.example.com/admin-panel
 website doesn’t exist!

In this example the star sign got replaced by the 4 words in the database or the wordlist text file and then the new replaced url got fetched, the results show that the 1st three urls seem to actually have a functioning website on the internet while the last one does not as it seems to be an invalid url.

