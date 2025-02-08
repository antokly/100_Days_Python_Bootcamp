import random

def computer_chose_number(min_nb, max_nb):
    """Select a random number in range(min_nb, max_nb)."""
    return random.randint(min_nb, max_nb)

def init_attempts_number(mode):
    """Initialize the number of attempts based on difficulty mode."""
    return 10 if mode == "hard" else 5

def check_attempts(attempts_nb):
    """Check if the player has attempts left."""
    return attempts_nb <= 0

def is_right_number(num, selected_num):
    """Check if the guessed number is correct and give hints."""
    if num == selected_num:
        print(f"You got it! The answer was {selected_num}.")
        return True
    elif num < selected_num:
        print("Too low! Guess again.")
    else:
        print("Too high! Guess again.")
    return False

def GuessTheNumber():
    """Main function to run the guessing game."""
    print("Welcome to Guess The Number Game!")

    minLimit = int(input("Choose the min limit: "))
    maxLimit = int(input("Choose the max limit: "))

    # Select a random number within limits
    computer_nbr = computer_chose_number(minLimit, maxLimit)

    # Ask user for mode: "easy" or "hard"
    user_mode = input("Choose difficulty (easy/hard): ").strip().lower()
    while user_mode not in ["easy", "hard"]:
        user_mode = input("Invalid choice! Choose difficulty (easy/hard): ").strip().lower()

    # Initialize attempts number
    attempts_nbr = init_attempts_number(user_mode)

    #Logic Loop of the game
    while attempts_nbr > 0: 
        try:
            user_nbr = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if is_right_number(user_nbr, computer_nbr):
            break
        else:
            attempts_nbr -= 1
            print(f"You have {attempts_nbr} attempts remaining.")

        if check_attempts(attempts_nbr):
            print(f"You've run out of guesses! The correct number was {computer_nbr}. You lose.")
            break

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        GuessTheNumber()

GuessTheNumber()