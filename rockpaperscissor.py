import tkinter as tk
import random

def play_game():
    user_choice = entry.get().lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "You lose!"

def reset_game():
    entry.delete(0, tk.END)
    result_label.config(text="")

def exit_game():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.config(bg = 'pink')
# Labels
label = tk.Label(root, text="Enter your choice (rock, paper, or scissors):")
label.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Entry
entry = tk.Entry(root)
entry.pack(pady=10)

# Buttons
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
