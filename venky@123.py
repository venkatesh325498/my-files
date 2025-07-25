import tkinter as tk
from tkinter import messagebox
import csv
import random

def register_voter():
    name = entry_name.get()
    dob = entry_dob.get()
    address = entry_address.get()
    gender = gender_var.get()

    if not name or not dob or not address or not gender:
        messagebox.showerror("Error", "Please fill all the fields.")
        return

    # Generate a simple Voter ID (random 6 digit number)
    voter_id = f"VOTER{random.randint(100000, 999999)}"

    # Save to CSV file
    with open("voters.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([voter_id, name, dob, address, gender])

    messagebox.showinfo("Success", f"Voter Registered!\nYour Voter ID: {voter_id}")

    # Clear the fields after registration
    entry_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    gender_var.set(None)

# Create the main window
root = tk.Tk()
root.title("Voter ID Registration")

# Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(root, text="Date of Birth (DD/MM/YYYY):").grid(row=1, column=0, pady=5)
entry_dob = tk.Entry(root)
entry_dob.grid(row=1, column=1, pady=5)

tk.Label(root, text="Address:").grid(row=2, column=0, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=2, column=1, pady=5)

tk.Label(root, text="Gender:").grid(row=3, column=0, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4, column=1, sticky="w")

# Register button
register_button = tk.Button(root, text="Register", command=register_voter)
register_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
