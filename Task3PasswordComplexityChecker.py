import re
import tkinter as tk
from tkinter import messagebox


def assess_password_strength(password):
    criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Uppercase Letter": bool(re.search(r'[A-Z]', password)),
        "Lowercase Letter": bool(re.search(r'[a-z]', password)),
        "Number": bool(re.search(r'\d', password)),
        "Special Character": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    feedback = []
    score = 0

    for criterion, passed in criteria.items():
        if passed:
            feedback.append(f"✓ {criterion}")
            score += 1
        else:
            feedback.append(f"✗ {criterion}")

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


def check_password():
    password = entry.get()
    strength, feedback = assess_password_strength(password)

    result = "\n".join(feedback) + f"\n\nOverall Password Strength: {strength}"
    messagebox.showinfo("Password Strength Checker", result)


# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Check Strength", command=check_password)
button.pack(pady=10)

root.mainloop()
