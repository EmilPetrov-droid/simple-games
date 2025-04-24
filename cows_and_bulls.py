import tkinter as tk
from tkinter import messagebox
import random

# Generate a 4-digit number with unique digits
target_number = random.sample([str(x) for x in range(10)], 4)
attempts = 0

def check_guess(event=None):
    global attempts
    guess = entry.get()

    if len(guess) != 4 or not guess.isdigit():
        messagebox.showwarning("Invalid input", "Enter exactly 4 digits.")
        entry.delete(0, tk.END)
        return

    if len(set(guess)) < 4:
        messagebox.showwarning("Invalid input", "Digits must be unique.")
        entry.delete(0, tk.END)
        return

    attempts += 1
    cows = 0
    bulls = 0

    for i in range(4):
        if guess[i] == target_number[i]:
            bulls += 1
        elif guess[i] in target_number:
            cows += 1

    if bulls == 4:
        messagebox.showinfo("Congratulations!", f"You guessed it in {attempts} attempts!")
        root.quit()
    else:
        result_label.config(text=f"{cows} cow(s), {bulls} bull(s) — Attempt #{attempts}")
    entry.delete(0, tk.END)

def give_up():
    number = ''.join(target_number)
    messagebox.showinfo("You gave up!", f"The correct number was: {number}")
    root.quit()

# Tkinter setup
root = tk.Tk()
root.title("Cows and Bulls - Full Number Entry")

tk.Label(root, text="Enter a 4-digit number with unique digits:").pack(pady=5)

entry = tk.Entry(root, font=("Arial", 18), width=10, justify="center")
entry.pack(pady=5)
entry.focus()
entry.bind("<Return>", check_guess)        # Main Enter key
entry.bind("<KP_Enter>", check_guess)     # Numpad Enter key

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

check_button = tk.Button(button_frame, text="Check", command=check_guess)
check_button.pack(side=tk.LEFT, padx=5)
check_button.bind("<Return>", lambda e: check_guess())  # Enter works on Check button
check_button.bind("<KP_Enter>", lambda e: check_guess())  # Numpad Enter works too

give_up_button = tk.Button(button_frame, text="Give Up", command=give_up)
give_up_button.pack(side=tk.LEFT, padx=5)
give_up_button.bind("<Return>", lambda e: give_up())  # Optional: Main Enter on Give Up
give_up_button.bind("<KP_Enter>", lambda e: give_up())  # Optional: Numpad Enter on Give Up

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
