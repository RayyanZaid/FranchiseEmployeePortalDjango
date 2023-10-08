import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("mySQL_PASSWORD")

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(user='root', password=password, host='127.0.0.1', database="sql_store")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Define your SQL query to retrieve all rows from the 'sql_store' table
    query = "SELECT * FROM customers"

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Iterate through the rows and print each row
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    # Close the cursor and connection when done
    if cursor:
        cursor.close()
    if connection.is_connected():
        connection.close()
