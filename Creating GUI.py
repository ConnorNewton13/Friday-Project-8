import sqlite3

def create_database():
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_database()
import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END).strip()
    
    if name and email and feedback:
        save_to_database(name, email, feedback)
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def save_to_database(name, email, feedback):
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)
    ''', (name, email, feedback))
    conn.commit()
    conn.close()

# Create main application window
app = tk.Tk()
app.title("Customer Feedback")

# Create input fields
tk.Label(app, text="Name").pack()
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Email").pack()
entry_email = tk.Entry(app)
entry_email.pack()

tk.Label(app, text="Feedback").pack()
entry_feedback = tk.Text(app, height=10, width=30)
entry_feedback.pack()

# Create submit button
submit_button = tk.Button(app, text="Submit", command=submit_feedback)
submit_button.pack()

app.mainloop()
def retrieve_data():
    password = input("Enter password to access feedback data: ")
    if password == "your_secure_password":  # Replace with your actual password
        conn = sqlite3.connect('customer_feedback.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM feedback')
        entries = cursor.fetchall()
        conn.close()

        if entries:
            for entry in entries:
                print(f"ID: {entry[0]}, Name: {entry[1]}, Email: {entry[2]}, Feedback: {entry[3]}")
        else:
            print("No feedback entries found.")
    else:
        print("Access denied: Incorrect password.")