# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (computer_choice == "r") and (user_choice == "p"):
    print(f"You won! {user_choice} beats {computer_choice}")
elif (computer_choice == "r") and (user_choice == "s"):
    print(f"You lost! {computer_choice} beats {user_choice}")
elif (computer_choice == user_choice):
    print("It's a tie!")
elif (computer_choice == "p") and (user_choice == "r"):
    print(f"You lost! {computer_choice} beats {user_choice}")
elif (computer_choice == "p") and (user_choice == "s"):
    print(f"You won! {user_choice} beats {computer_choice}")
elif (computer_choice == "s") and (user_choice == "r"):
    print(f"You won! {user_choice} beats {computer_choice}")
elif (computer_choice == "s") and (user_choice == "p"):
    print(f"You lost! {computer_choice} beats {user_choice}")
else:
    print("Wrong input")
