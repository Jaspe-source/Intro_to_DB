#!/usr/bin/env python3
import mysql.connector

def main():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # add your password if needed
        )
        cursor = cnx.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    main()
