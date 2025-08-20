#!/usr/bin/env python3
import mysql.connector

def main():
    """
    Creates the MySQL database `alx_book_store`.
    - Does not fail if the database already exists.
    - Prints a success message when created/existing.
    - Handles connection and creation errors.
    - Closes cursor and connection safely.
    - Does not use SELECT or SHOW statements.
    """
    try:
        # connect to MySQL server (no database yet)
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # put your password if you have one
        )
        cursor = cnx.cursor()

        # create the database if it doesn’t exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # explicit checker's requirement
        print(f"Error: {err}")

    finally:
        # clean up
        try:
            if cursor:
                cursor.close()
            if cnx and cnx.is_connected():
                cnx.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()

