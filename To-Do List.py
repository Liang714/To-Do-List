import json
import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

"""def login():
    # Check the entered credentials
    if username_entry.get() == "admin" and password_entry.get() == "password":
        # If the credentials are correct, destroy the login window and open the main window
        login_window.destroy()
        main_window()
    else:
        # If the credentials are incorrect, show an error message
        messagebox.showerror("Error", "Incorrect username or password")
"""
def create_user(user):
    # Load the existing users
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    # Add the new user
    users[user[0]] = user[1]

    # Save the users
    with open('users.json', 'w') as f:
        json.dump(users, f)

def login():
    # Load the existing users
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    # Check the entered credentials
    user = (username_entry.get(), password_entry.get())
    if user[0] in users and users[user[0]] == user[1]:
        # If the credentials are correct, destroy the login window and open the main window
        login_window.destroy()
        main_window()
    else:
        # If the credentials are incorrect, show an error message
        messagebox.showerror("Error", "Incorrect username or password")

def sign_up():
    # Load the existing users
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    # Get the entered credentials
    user = (username_entry.get(), password_entry.get())

    # If the user ID already exists, show an error message
    if user[0] in users:
        messagebox.showerror("Error", "User ID already exists")
    else:
        # If the user ID doesn't exist, create a new user
        create_user(user)
        messagebox.showinfo("Success", "User created successfully")
           

def main_window():
    def add_task():
        task = entry.get()
        if task != "":
            # Get the number of the task
            task_number = listbox.size() + 1

            # Add the task to the listbox
            listbox.insert(tk.END, f"{task_number}. {task}")
            entry.delete(0, tk.END)


    def delete_item():
        # Get a list of indices of the selected items
        selected_indices = list(listbox.curselection())

        if selected_indices:  # If there are selected items
            # Reverse the list to avoid changing the indices of items that are yet to be deleted
            selected_indices.reverse()

            # Delete the selected items
            for index in selected_indices:
                listbox.delete(index)

    def clear_all_items():
        listbox.delete(0, tk.END)

    window = tk.Tk()
    window.title("To-Do LIST")
    window.attributes('-alpha')  # Make the window transparent
    background_image = tk.PhotoImage(file="/Users/liang/Desktop/Code/Python/page.png")
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    frame = tk.Frame(window)
    frame.pack(pady=10)


    listbox = tk.Listbox(
        frame,
        width=40,
        height=20,
        bd=0,
        font=("Courier New", 15, "bold"),
        selectbackground="#a6a6a6",
        bg="lightyellow",
        selectmode=tk.MULTIPLE
    )
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox.config(yscrollcommand=scrollbar.set)    
    scrollbar.config(command=listbox.yview)

    entry = tk.Entry(
        window,
        width=30,
        font=("Courier New", 12)
    )
    entry.pack(pady=10)

    button_frame = tk.Frame(window,bg="black")
    button_frame.pack(pady=10)

    photo = tk.PhotoImage(file="/Users/liang/Desktop/Code/Python/plus.png")
    photo = photo.subsample(10, 10)
    add_button = tk.Button(
        button_frame,
        image=photo,
        command=add_task
    )
    add_button.pack(side=tk.LEFT)
    add_button.image = photo

    photo = tk.PhotoImage(file="/Users/liang/Desktop/Code/Python/minus.png")
    photo = photo.subsample(10, 10)
    delete_button = tk.Button(
        button_frame,
        image=photo,
        command=delete_item,
    )
    delete_button.pack(side=tk.LEFT)
    delete_button.image = photo

    photo = tk.PhotoImage(file="/Users/liang/Desktop/Code/Python/clean.png")
    photo = photo.subsample(10, 10)
    clear_button = tk.Button(
        button_frame,
        image=photo,
        command=clear_all_items,
        
    )
    clear_button.pack(side=tk.LEFT)
    clear_button.image = photo

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Size of the application
    app_width = 500  # Replace with your application width
    app_height = 500  # Replace with your application height

    # Calculate the position of the top left corner of the window
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    # Set the size and position of the window
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    window.mainloop()

login_window = tk.Tk()
login_window.title("TO-DO LIST") 


# Load the GIF
to_do_image = tk.PhotoImage(file="/Users/liang/Desktop/Code/Python/to-do.png")
to_do_image = to_do_image.subsample(2, 2)

# Create a label with the GIF
todo_label = tk.Label(login_window, image=to_do_image)
todo_label.place(relx=0.5, rely=0.2, anchor='center')

title_label = tk.Label(login_window, text="Enter Login ID")
title_label.place(relx=0.5, rely=0.43, anchor='center')
title_label = tk.Label(login_window, text="Enter Password")
title_label.place(relx=0.5, rely=0.58, anchor='center')

# Create username and password entry fields
username_entry = tk.Entry(login_window)
username_entry.place(relx=0.5, rely=0.5, anchor='center')

password_entry = tk.Entry(login_window, show="*")
password_entry.place(relx=0.5, rely=0.65, anchor='center')
# Create a login button
sign_up_button = tk.Button(login_window, text="Sign Up", command=sign_up)
sign_up_button.place(relx=0.3, rely=0.8, anchor='center')
login_button = tk.Button(login_window, text="Login", command=login)
login_button.place(relx=0.7, rely=0.8, anchor='center')

screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()

# Size of the application
app_width = 350 # Replace with your application width
app_height = 350  # Replace with your application height

# Calculate the position of the top left corner of the window
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

# Set the size and position of the window
login_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
login_window.mainloop()