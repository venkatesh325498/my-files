import tkinter as tk
from tkinter import messagebox
import csv
import os

FILE = 'library.csv'

# Check if file exists; if not, create it with headers
if not os.path.exists(FILE):
    with open(FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Author', 'Year', 'ISBN', 'Quantity'])

def add_book(title, author, year, isbn, quantity):
    with open(FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([title, author, year, isbn, quantity])

def read_books():
    books = []
    with open(FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(row)
    return books

def add_book_gui():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    isbn = isbn_entry.get()
    quantity = quantity_entry.get()

    if title and author and year.isdigit() and isbn and quantity.isdigit():
        add_book(title, author, year, isbn, quantity)
        messagebox.showinfo("Success", "Book added!")
        clear_entries()
        refresh_list()
    else:
        messagebox.showerror("Error", "Please enter valid data")

def refresh_list():
    listbox.delete(0, tk.END)
    for book in read_books():
        listbox.insert(tk.END, f"{book['Title']} by {book['Author']} ({book['Year']}) - Qty: {book['Quantity']}")

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Library Management System")

# Labels and entries
tk.Label(root, text="Title").grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Author").grid(row=1, column=0)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1)

tk.Label(root, text="Year").grid(row=2, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1)

tk.Label(root, text="ISBN").grid(row=3, column=0)
isbn_entry = tk.Entry(root)
isbn_entry.grid(row=3, column=1)

tk.Label(root, text="Quantity").grid(row=4, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=4, column=1)

# Add Book button
tk.Button(root, text="Add Book", command=add_book_gui).grid(row=5, column=1)

# Listbox to display books
listbox = tk.Listbox(root, width=60)
listbox.grid(row=6, column=0, columnspan=2)

refresh_list()

root.mainloop()
