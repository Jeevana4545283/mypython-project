import tkinter as tk
import random

secret_number = random.randint(1, 100)
attempts_left = 7

def check_guess():
    global attempts_left
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            result_label.config(text="❗ Enter a number between 1 and 100.")
        elif guess < secret_number:
            attempts_left -= 1
            result_label.config(text=f"📉 Too low! Attempts left: {attempts_left}")
        elif guess > secret_number:
            attempts_left -= 1
            result_label.config(text=f"📈 Too high! Attempts left: {attempts_left}")
        else:
            result_label.config(text=f"✅ Correct! The number was {secret_number}")
            submit_button.config(state="disabled")
            return
        if attempts_left == 0:
            result_label.config(text=f"😞 Game Over! The number was {secret_number}")
            submit_button.config(state="disabled")
    except ValueError:
        result_label.config(text="❗ Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")

title_label = tk.Label(root, text="🎯 Guess the Number (1-100)", font=("Helvetica", 16))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit Guess", command=check_guess, font=("Helvetica", 12))
submit_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()