import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

# Function to check password strength and return level + hints
def check_strength(password):
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[@$!%*?&.#^_()-]', password)

    score = 0
    hints = []

    if length >= 8:
        score += 1
    else:
        hints.append("Use at least 8 characters.")

    if has_upper:
        score += 1
    else:
        hints.append("Add uppercase letters (A-Z).")

    if has_lower:
        score += 1
    else:
        hints.append("Add lowercase letters (a-z).")

    if has_digit:
        score += 1
    else:
        hints.append("Add numbers (0-9).")

    if has_special:
        score += 1
    else:
        hints.append("Add special characters (!, @, #, etc).")

    if score <= 2:
        return "Weak", "red", hints
    elif score == 3 or score == 4:
        return "Medium", "orange", hints
    else:
        return "Very Strong", "green", []

# Toggle password visibility
def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text='👁️')
    else:
        entry.config(show='')
        toggle_btn.config(text='🙈')

# Event to update strength display
def update_strength(*args):
    pwd = password_var.get()
    level, color, tips = check_strength(pwd)

    strength_label.config(text=f"Strength: {level}", foreground=color)
    progress['value'] = {"Weak": 30, "Medium": 60, "Very Strong": 100}[level]
    progress.config(style=f"{color}.Horizontal.TProgressbar")

    if pwd == "":
        hints_box.config(text="")
    elif level == "Very Strong":
        hints_box.config(text="✅ Excellent password!")
    else:
        hints_box.config(text="❗Tips:\n- " + "\n- ".join(tips))

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker ")
root.geometry("400x320")
root.resizable(False, False)

style = ttk.Style()
style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
style.configure("orange.Horizontal.TProgressbar", foreground='orange', background='orange')
style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

# Password input label
tk.Label(root, text="Enter Password:", font=("Segoe UI", 12)).pack(pady=(20, 5))

frame = tk.Frame(root)
frame.pack()

password_var = tk.StringVar()
password_var.trace_add("write", update_strength)

entry = ttk.Entry(frame, textvariable=password_var, show='*', width=30, font=("Segoe UI", 12))
entry.pack(side='left', padx=5)

toggle_btn = tk.Button(frame, text='👁️', font=("Segoe UI", 10), command=toggle_password)
toggle_btn.pack(side='left')

# Strength label
strength_label = tk.Label(root, text="Strength: ", font=("Segoe UI", 12, "bold"))
strength_label.pack(pady=10)

# Progress bar
progress = ttk.Progressbar(root, length=250, mode='determinate')
progress.pack(pady=5)

# Hints display
hints_box = tk.Label(root, text="", font=("Segoe UI", 10), justify="left", fg="gray")
hints_box.pack(pady=(10, 0))

# Run
root.mainloop()
