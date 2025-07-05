import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    mydb = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )
    mycursor = mydb.cursor()
    return mydb, mycursor


# mydb, mycursor = get_db_connection()
# mycursor.execute("DROP TABLE IF EXISTS expenses")
# mycursor.execute("CREATE TABLE expenses (user_name VARCHAR(20), category VARCHAR(20) NOT NULL, description VARCHAR(20) NOT NULL, amount INT NOT NULL, date VARCHAR(10) NOT NULL);")

# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)