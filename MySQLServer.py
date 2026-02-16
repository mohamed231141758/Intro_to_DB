import mysql.connector
from mysql.connector import Error

connection = None

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        cursor.close()

except Error as e:
    print(f"Error: Unable to connect to MySQL server. {e}")

finally:
    if connection is not None and connection.is_connected():
        connection.close()
