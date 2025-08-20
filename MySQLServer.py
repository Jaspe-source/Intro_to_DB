import os
import sys
import mysql.connector
from mysql.connector import Error

def main() -> None:
    """
    Creates the MYSQL database 'alx_book_store' on the connected server.
    - Does not fail if it already exists (IF NOT EXISTS).
    - Prints a success message
    - Prints a clear error message on failure.
    properly opens and closes the connection.
    - Does not use SELECT or SHOW statements.
    """

    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")

    try:
        port = int(os.getenv("MYSQL_PORT", "3306"))
    except ValueError:
        port = 3306

    cnx = None
    cursor = None

    try:
        # Connect without specifying a database
        cnx = mysql.connector.connect(
            host=host, port=port, user=user, password=password
        )
    except Error as e:
        print(f"Error connecting to MYSQL: {e}")
        sys.exit(1)

    try:
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error creating database: {e}")
        sys.exit(1)

    finally:
        try:
            if cnx is not None and cnx.is_connected():
                cnx.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
