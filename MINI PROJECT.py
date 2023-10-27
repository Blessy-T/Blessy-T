import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Create a Tkinter window
root = tk.Tk()
root.title("College Application Form")

# Create a frame for the application form
form_frame = ttk.Frame(root)

# Create labels for the application form fields
name_label = ttk.Label(form_frame, text="Name")
email_label = ttk.Label(form_frame, text="Email")
phone_number_label = ttk.Label(form_frame, text="Phone Number")
gender_label = ttk.Label(form_frame, text="gender")
age_label = ttk.Label(form_frame, text="age")
percentage_label = ttk.Label(form_frame, text="percentage")

# Create entry widgets for the application form fields
name_entry = ttk.Entry(form_frame)
email_entry = ttk.Entry(form_frame)
phone_number_entry = ttk.Entry(form_frame)
gender_entry = ttk.Entry(form_frame)
age_entry = ttk.Entry(form_frame)
percentage_entry = ttk.Entry(form_frame)

# Create a frame for the submit button
submit_frame = ttk.Frame(root)

# Create a submit button
submit_button = ttk.Button(submit_frame, text="Submit")

# Bind the submit button to a function that will save the application form data to the database
submit_button.config(command=lambda: save_application_form_data())

# Add the labels and entry widgets to the application form frame
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)
phone_number_label.grid(row=2, column=0)
phone_number_entry.grid(row=2, column=1)
gender_label.grid(row=3, column=0)
gender_entry.grid(row=3, column=1)
age_label.grid(row=4, column=0)
age_entry.grid(row=4, column=1)
percentage_label.grid(row=5, column=0)
percentage_entry.grid(row=5, column=1)

# Add the submit button to the submit frame
submit_button.grid(row=0, column=0)

# Pack the application form frame and submit frame
form_frame.pack()
submit_frame.pack()

# Create a database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="mydatabase"
)

# Create a cursor object
cursor = connection.cursor()


# Save the application form data to the database
def save_application_form_data():
    name = name_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    gender = gender_entry.get()
    age = age_entry.get()
    percentage = percentage_entry.get()

    cursor.execute("""
    INSERT INTO application_form (name, email, phone_number, gender, age, percentage)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, email, phone_number, gender, age, percentage))

    connection.commit()

    messagebox.showinfo("Success", "Application form data saved successfully")

# Run the application
root.mainloop()
