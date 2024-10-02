import tkinter as tk
from tkinter import messagebox
import random

# Function to start the game and generate a random number
def start_game():
    global random_number
    random_number = random.randint(1, 100)  # Generates a number between 1 and 100
    label_result.config(text="Guess a number between 1 and 100")
    entry_guess.config(state="normal")  # Enable input for guessing
    button_check.config(state="normal")  # Enable the check button

# Function to check the user's guess
def check_guess():
    try:
        user_guess = int(entry_guess.get())
        if user_guess < 1 or user_guess > 100:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100.")
        else:
            if user_guess < random_number:
                label_result.config(text="Too low! Try again.")
            elif user_guess > random_number:
                label_result.config(text="Too high! Try again.")
            else:
                label_result.config(text=f"Congratulations! You guessed it right, the number was {random_number}.")
                entry_guess.config(state="disabled")  # Disable further input after a correct guess
                button_check.config(state="disabled")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Random Number Guessing Game")
root.geometry("300x200")

# Create the input fields and labels
label_title = tk.Label(root, text="Random Number Guessing Game", font=("Arial", 14))
label_title.pack(pady=10)

label_instruction = tk.Label(root, text="Click 'Start' to begin the game.")
label_instruction.pack(pady=5)

button_start = tk.Button(root, text="Start Game", command=start_game)
button_start.pack(pady=10)

entry_guess = tk.Entry(root, width=10, state="disabled")
entry_guess.pack(pady=5)

button_check = tk.Button(root, text="Check Guess", state="disabled", command=check_guess)
button_check.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the main loop
root.mainloop()
