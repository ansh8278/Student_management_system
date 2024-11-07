import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="@Ansh12345678",  
        database="student_db"
    )

# Function to add a student
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    major = entry_major.get()

    if name and age.isdigit() and major:
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO students (name, age, major) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, int(age), major))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully!")
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_major.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please provide valid input.")

# Function to view all students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    cursor.close()
    conn.close()

    output_text.delete("1.0", tk.END)
    for record in records:
        output_text.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Major: {record[3]}\n")

# Function to delete a student by ID
def delete_student():
    student_id = entry_delete_id.get()
    if student_id.isdigit():
        conn = connect_db()
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Student deleted successfully!")
        entry_delete_id.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please provide a valid ID.")

# Create the main window
window = tk.Tk()
window.title("Student Management System")

# Input fields
tk.Label(window, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

tk.Label(window, text="Age").grid(row=1, column=0)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1)

tk.Label(window, text="Major").grid(row=2, column=0)
entry_major = tk.Entry(window)
entry_major.grid(row=2, column=1)

# Buttons
tk.Button(window, text="Add Student", command=add_student).grid(row=3, column=1)
tk.Button(window, text="View Students", command=view_students).grid(row=4, column=1)

# Output display
output_text = tk.Text(window, height=10, width=50)
output_text.grid(row=5, column=0, columnspan=2)

# Delete section
tk.Label(window, text="Enter ID to Delete").grid(row=6, column=0)
entry_delete_id = tk.Entry(window)
entry_delete_id.grid(row=6, column=1)
tk.Button(window, text="Delete Student", command=delete_student).grid(row=7, column=1)

# Run the application
window.mainloop()
