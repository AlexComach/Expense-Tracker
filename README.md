# Expense Tracker
This is an expense tracker made in Python where you can log, store, switch user and breakdown log inputs. It is connected to an SQL Database so all data thats stored will go to the database.

## How it's made
**Tech used** Python, SQL
In this project, it asks for a user, and then gives you options to log an expense, view the expenses that have been logged by that user, change user, breakdown expenses of the current user and end. I separated 
it into 4 different files, one for the function, one for connecting to the Database, one for testing and one for running. For the function file, I have 4 functions, 
log_expense, view_list, store_data and breakdown. log_expense make the log a current log, which is then passed to store_data, which will store the log data to the database. view_list
will allow user to only view the user's expense logs, and breakdown will group up match categories, add it up and then add everything the user has purchased into a total, which is shown in a table. Only the current users expenses will be shown. Breakdown will also show the percentage of wage used on every category and also show the amount of money left. For Expense_Tracker I used tabulate, and datetime libraries. For test_tracker, I used pytest to check that all inputs give valid outputs. For the connect_to_db file, I user the library called mysql.connector. My run_tracker allows me to run the functions in a neat format within the python terminal.

## Lessons learned:
This project has taught me how I can get Python to interact with an SQL database, and also has improved my logical reasoning skills, especially when
creating the breakdown function. Creating the breakdown function required me to manipulate dictionaries, which has helped me gain a deeper
understand of how dictionaries can be updated, deleted from and using the content in any way I want. 

## Aspirations for this project:
I would like make the run_tracker interactive with a GUI, and also explore what I can do with sql.connector. Maybe create an admin
account that can access, view, update and delete logs that have been stored in the database.

**Video Demo:** https://youtu.be/lb4RyU40ZyU?si=0X59tS1HKj74VH7R

