import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os

# File name
FILE_NAME = "expenses.csv"

# Create CSV if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)

# Function to add expense
def add_expense():

    category = category_var.get()
    amount = amount_entry.get()

    if category == "" or amount == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Enter valid amount")
        return

    # Save to CSV
    new_data = pd.DataFrame({
        "Category": [category],
        "Amount": [amount]
    })

    new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)

    messagebox.showinfo("Success", "Expense Added")

    amount_entry.delete(0, tk.END)

# Function to show graph
def show_graph():

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        messagebox.showerror("Error", "No expenses found")
        return

    category_total = df.groupby("Category")["Amount"].sum()

    # Bar Graph
    category_total.plot(kind='bar')

    plt.title("Expense Tracker")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()

# Main Window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")
root.config(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="Expense Tracker",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
heading.pack(pady=20)

# Category
tk.Label(root, text="Category", bg="lightblue",
         font=("Arial", 12)).pack()

category_var = tk.StringVar()

category_box = ttk.Combobox(
    root,
    textvariable=category_var,
    values=["Food", "Travel", "Shopping", "Bills", "Others"]
)

category_box.pack(pady=10)

# Amount
tk.Label(root, text="Amount", bg="lightblue",
         font=("Arial", 12)).pack()

amount_entry = tk.Entry(root, width=25)
amount_entry.pack(pady=10)

# Add Button
add_btn = tk.Button(
    root,
    text="Add Expense",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=add_expense
)

add_btn.pack(pady=10)

# Graph Button
graph_btn = tk.Button(
    root,
    text="Show Graph",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    command=show_graph
)

graph_btn.pack(pady=10)
print("app running")

root.mainloop()