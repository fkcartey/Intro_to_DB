import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connecting to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Creating the database using IF NOT EXISTS to avoid errors if it exists
            # We avoid SELECT/SHOW as per requirements
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error:
        # Handling connection errors specifically
        print("Error: Could not connect to MySQL server.")
    
    finally:
        # Handling the closing of the database/connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
