import mysql.connector
from expense_tracker import log_expense, view_list, store_data, breakdown, user_list, user_list_duplicate, tracker
from tabulate import tabulate

mydb = mysql.connector.connect(host="localhost", user="root", passwd="P127813986$a", database="expensetrackerdatabase")

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS expenses")
mycursor.execute("CREATE TABLE expenses (user_name VARCHAR(20), category VARCHAR(20) NOT NULL, description VARCHAR(20) NOT NULL, amount INT NOT NULL);")

mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)