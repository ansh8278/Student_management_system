import tkinter as tk
from tkinter import messagebox, ttk
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
    if records:
        for record in records:
            output_text.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Major: {record[3]}\n")
    else:
        output_text.insert(tk.END, "No records found.")

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

# Function to search for a student by name
def search_student():
    name = entry_search_name.get()
    if name:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM students WHERE name LIKE %s"
        cursor.execute(query, (f"%{name}%",))
        records = cursor.fetchall()
        cursor.close()
        conn.close()

        output_text.delete("1.0", tk.END)
        if records:
            for record in records:
                output_text.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Major: {record[3]}\n")
        else:
            output_text.insert(tk.END, "No matching records found.")
    else:
        messagebox.showwarning("Input Error", "Please enter a name to search.")

# Function to clear the output text
def clear_output():
    output_text.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Enhanced Student Management System")
window.geometry("600x500")
window.resizable(True, True)

# Frame for input fields and buttons
frame_input = ttk.Frame(window, padding="10")
frame_input.grid(row=0, column=0, sticky="ew")

# Input fields
ttk.Label(frame_input, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_name = ttk.Entry(frame_input)
entry_name.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="Age").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_age = ttk.Entry(frame_input)
entry_age.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="Major").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_major = ttk.Entry(frame_input)
entry_major.grid(row=2, column=1, padx=5, pady=5)

# Buttons
ttk.Button(frame_input, text="Add Student", command=add_student).grid(row=3, column=1, padx=5, pady=5, sticky="e")
ttk.Button(frame_input, text="View All Students", command=view_students).grid(row=4, column=1, padx=5, pady=5, sticky="e")

# Frame for output display and actions
frame_output = ttk.Frame(window, padding="10")
frame_output.grid(row=1, column=0, sticky="nsew")

# Output display
output_text = tk.Text(frame_output, height=15, width=60, wrap="word")
output_text.grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_output, text="Clear Output", command=clear_output).grid(row=1, column=0, padx=5, pady=5, sticky="e")

# Frame for deletion and search
frame_delete_search = ttk.Frame(window, padding="10")
frame_delete_search.grid(row=2, column=0, sticky="ew")

# Delete section
ttk.Label(frame_delete_search, text="Enter ID to Delete").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_delete_id = ttk.Entry(frame_delete_search)
entry_delete_id.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_delete_search, text="Delete Student", command=delete_student).grid(row=0, column=2, padx=5, pady=5)

# Search section
ttk.Label(frame_delete_search, text="Search by Name").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_search_name = ttk.Entry(frame_delete_search)
entry_search_name.grid(row=1, column=1, padx=5, pady=5)
ttk.Button(frame_delete_search, text="Search", command=search_student).grid(row=1, column=2, padx=5, pady=5)

# Configure window resizing
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Run the application
window.mainloop()
