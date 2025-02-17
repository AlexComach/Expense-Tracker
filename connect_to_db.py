import mysql.connector

def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd="P127813986$a", 
        database="expensetrackerdatabase")
    
    mycursor = mydb.cursor()
    return mydb, mycursor


mydb, mycursor = get_db_connection()
mycursor.execute("DROP TABLE IF EXISTS expenses")
mycursor.execute("CREATE TABLE expenses (user_name VARCHAR(20), category VARCHAR(20) NOT NULL, description VARCHAR(20) NOT NULL, amount INT NOT NULL, date VARCHAR(10) NOT NULL);")

# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)