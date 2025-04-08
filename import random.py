import tkinter as tk
import random

# Global variables
target_number = 0
attempts_left = 0

# Function to set difficulty and start the game
def start_game(mode):
    global target_number, attempts_left
    if mode == "Easy":
        target_number = random.randint(1, 50)  # Smaller range for Easy mode
        attempts_left = 10
    elif mode == "Medium":
        target_number = random.randint(1, 100)
        attempts_left = 7
    elif mode == "Hard":
        target_number = random.randint(1, 200)  # Larger range for Hard mode
        attempts_left = 5
    
    feedback_label.config(text=f"Mode: {mode} | You have {attempts_left} attempts. Guess the number!", fg="black")
    entry.delete(0, tk.END)

# Function to check the guess
def check_guess():
    global attempts_left
    guess = entry.get()
    if not guess.isdigit():
        feedback_label.config(text="Please enter a valid number!", fg="red")
        return
    
    guess = int(guess)
    attempts_left -= 1

    if guess == target_number:
        feedback_label.config(text="🎉 Correct! You guessed the number!", fg="green")
        submit_button.config(state="disabled")
    elif attempts_left == 0:
        feedback_label.config(text=f"😢 Out of attempts! The correct number was {target_number}.", fg="red")
        submit_button.config(state="normal")
    elif guess < target_number:
        feedback_label.config(text=f"Too low! Attempts left: {attempts_left}", fg="blue")
    else:
        feedback_label.config(text=f"Too high! Attempts left: {attempts_left}", fg="blue")

# Function to restart the game
def restart_game():
    submit_button.config(state="normal")
    feedback_label.config(text="Select a mode to start the game!", fg="black")
    entry.delete(0, tk.END)

# Set up the GUI window
root = tk.Tk()
root.title("Number Guessing Game with Modes")

# Add widgets for mode selection
tk.Label(root, text="Select Difficulty Level:", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Easy", command=lambda: start_game("Easy"), font=("Arial", 12), bg="lightgreen").pack(pady=5)
tk.Button(root, text="Medium", command=lambda: start_game("Medium"), font=("Arial", 12), bg="lightblue").pack(pady=5)
tk.Button(root, text="Hard", command=lambda: start_game("Hard"), font=("Arial", 12), bg="orange").pack(pady=5)

# Add entry for guesses
entry = tk.Entry(root, width=10, font=("Arial", 14))
entry.pack(pady=10)

# Add buttons for submission and restart
submit_button = tk.Button(root, text="Submit Guess", command=check_guess, font=("Arial", 12), bg="yellow")
submit_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart Game", command=restart_game, font=("Arial", 12), bg="red")
restart_button.pack(pady=10)

# Add feedback label
feedback_label = tk.Label(root, text="Select a mode to start the game!", font=("Arial", 12), fg="black")
feedback_label.pack(pady=10)

# Run the GUI
root.mainloop()