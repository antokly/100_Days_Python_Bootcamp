# Rock, Paper, Scissors Game

import random

rock = "rock"

paper = "paper"

scissors = "scissors"

player_choice = input("What do you choose? Type 'rock', 'paper' or 'scissors'.\n> ").lower()

computer_choice = random.choice([rock, paper, scissors])

print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a draw.")
elif player_choice == rock:
    if computer_choice == paper:
        print("You lose.")
    else:
        print("You win.")
elif player_choice == paper:
    if computer_choice == scissors:
        print("You lose.")
    else:
        print("You win.")
elif player_choice == scissors:
    if computer_choice == rock:
        print("You lose.")
    else:
        print("You win.")
else:
    print("Please enter a valid choice.")

