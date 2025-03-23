import mysql.connector
from Account_Class import *
import Main_menu
import PINCheck
import tkinter as tk

def data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="credit_card"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CARD")

    for row in cursor.fetchall():
        Account(row[0], row[1], row[2], row[3])

    db.close()

def main():
    data()
    PINCheck.EnterPIN()

if __name__ == "__main__":
    main()
