import tkinter as tk
from tkinter import messagebox
import random
import string
import webbrowser
import pyperclip

# Dictionary database
url_database = {}

# Generate short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

# Shorten URL
def shorten_url():

    long_url = url_entry.get()

    if long_url == "":
        messagebox.showerror("Error", "Please enter URL")
        return

    short_code = generate_short_code()

    short_url = "short.ly/" + short_code

    # Save in database
    url_database[short_url] = long_url

    # Show short URL
    result_label.config(text=short_url)

# Copy URL
def copy_url():

    short_url = result_label.cget("text")

    if short_url != "":
        pyperclip.copy(short_url)
        messagebox.showinfo("Copied", "Short URL copied!")

# Open Original URL
def open_url():

    short_url = result_label.cget("text")

    if short_url in url_database:
        webbrowser.open(url_database[short_url])

    else:
        messagebox.showerror("Error", "URL not found")


# Main window
root = tk.Tk()

root.title("Python URL Shortener")
root.geometry("550x400")
root.config(bg="#f4f4f4")

# Heading
heading = tk.Label(
    root,
    text="URL Shortener",
    font=("Arial", 24, "bold"),
    bg="#f4f4f4",
    fg="blue"
)

heading.pack(pady=20)

# URL Entry
url_entry = tk.Entry(
    root,
    width=50,
    font=("Arial", 14)
)

url_entry.pack(pady=10)

# Shorten Button
shorten_button = tk.Button(
    root,
    text="Shorten URL",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    padx=10,
    pady=5,
    command=shorten_url
)

shorten_button.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    bg="#f4f4f4",
    fg="green"
)

result_label.pack(pady=20)

# Copy Button
copy_button = tk.Button(
    root,
    text="Copy URL",
    font=("Arial", 12),
    bg="green",
    fg="white",
    padx=10,
    pady=5,
    command=copy_url
)

copy_button.pack(pady=10)

# Open Button
open_button = tk.Button(
    root,
    text="Open Original URL",
    font=("Arial", 12),
    bg="orange",
    fg="white",
    padx=10,
    pady=5,
    command=open_url
)

open_button.pack(pady=10)

# Run Application
root.mainloop()