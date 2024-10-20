import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish connection to MySQL server
        conn = mysql.connector.connect(
            host="localhost",  # Change to your host if needed
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        cursor = conn.cursor()

        # Try to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
        finally:
            cursor.close()

    except mysql.connector.Error as err:
        # Handle connection errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        # Close the connection if everything is successful
        conn.close()

if __name__ == "__main__":
    create_database()
