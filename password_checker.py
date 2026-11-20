
import tkinter as tk
from tkinter import ttk
import re

def check_password():

    password = entry.get()

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character")

    if password == "":
        result.config(text="Enter a password", fg="white")
        progress["value"] = 0
        suggestion.config(text="")
        return

    if score <= 2:
        result.config(text="WEAK PASSWORD", fg="red")

    elif score <= 4:
        result.config(text="MEDIUM PASSWORD", fg="orange")

    else:
        result.config(text="STRONG PASSWORD", fg="green")

    progress["value"] = score / 6 * 100

    if suggestions:
        suggestion.config(
            text="Suggestions:\n" + "\n".join(suggestions)
        )
    else:
        suggestion.config(
            text="Great! All requirements are satisfied."
        )


def toggle_password():

    if entry.cget("show") == "*":
        entry.config(show="")
        show_button.config(text="Hide")
    else:
        entry.config(show="*")
        show_button.config(text="Show")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x450")
root.configure(bg="#172033")
root.resizable(False, False)

heading = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 20, "bold"),
    bg="#172033",
    fg="white"
)
heading.pack(pady=25)

instruction = tk.Label(
    root,
    text="Enter your password below",
    font=("Arial", 11),
    bg="#172033",
    fg="white"
)
instruction.pack()

entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 14),
    show="*"
)
entry.pack(pady=15)

show_button = tk.Button(
    root,
    text="Show",
    command=toggle_password
)
show_button.pack()

check_button = tk.Button(
    root,
    text="Check Password",
    command=check_password,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold")
)
check_button.pack(pady=20)

result = tk.Label(
    root,
    text="Password Strength: Not Checked",
    font=("Arial", 14, "bold"),
    bg="#172033",
    fg="white"
)
result.pack(pady=10)

progress = ttk.Progressbar(
    root,
    length=300,
    maximum=100,
    mode="determinate"
)
progress.pack(pady=10)

suggestion = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#172033",
    fg="white",
    justify="left"
)
suggestion.pack(pady=15)

root.mainloop()
