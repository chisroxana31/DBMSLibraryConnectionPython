import tkinter as tk
from tkinter import messagebox
import mysql.connector
from threading import Thread

def insert_book():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="252525",
            database="labormap"
        )

        mycursor = mydb.cursor()

        # Get values from entry fields
        id_val = int(id_entry.get())
        title_val = title_entry.get()
        stock_val = int(stock_entry.get())

        # Insert data into the database
        sql = "INSERT INTO book (id, title, stock) VALUES (%s, %s, %s)"
        val = (id_val, title_val, stock_val)
        mycursor.execute(sql, val)

        mydb.commit()
        messagebox.showinfo("Success", "Book inserted successfully")

    except mysql.connector.Error as e:
        messagebox.showerror("Error", str(e))

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

def concurrent_transactions():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="252525",
            database="labormap"
        )

        mycursor = mydb.cursor()

        # Set isolation level to READ UNCOMMITTED
        mycursor.execute("SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")

        # Transaction 1: Read uncommitted data
        mycursor.execute("SELECT * FROM book")
        books1 = mycursor.fetchall()
        messagebox.showinfo("Transaction 1", f"Books (Uncommitted): {books1}")

        # Transaction 2: Insert a new book
        insert_book()

        # Transaction 1: Read committed data
        mycursor.execute("SELECT * FROM book")
        books2 = mycursor.fetchall()
        messagebox.showinfo("Transaction 1", f"Books (Committed): {books2}")

    except mysql.connector.Error as e:
        messagebox.showerror("Error", str(e))

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

# Create the main window
root = tk.Tk()
root.title("Library Management System")

# Create entry fields and labels
id_label = tk.Label(root, text="Book ID:")
id_label.grid(row=0, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5)

title_label = tk.Label(root, text="Title:")
title_label.grid(row=1, column=0, padx=10, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1, padx=10, pady=5)

stock_label = tk.Label(root, text="Stock:")
stock_label.grid(row=2, column=0, padx=10, pady=5)
stock_entry = tk.Entry(root)
stock_entry.grid(row=2, column=1, padx=10, pady=5)

# Create a button to perform concurrent transactions
concurrent_button = tk.Button(root, text="Concurrent Transactions", command=concurrent_transactions)
concurrent_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI application
root.mainloop()
