# PyPassword Generator

print("Welcome to the PyPassword Generator.")

# import random module  
import random

for _ in range(3):
    # ask for number of letters
    while True:
        num_letters = input("How many letters would you like in your password?\n> ")
        if num_letters.strip():
            break
        else:
            print("Please enter a valid number of letters.")

    # ask for number of symbols
    while True:
        num_symbols = input("How many symbols would you like?\n> ")
        if num_symbols.strip():
            break
        else:
            print("Please enter a valid number of symbols.")

    # ask for number of numbers
    while True:
        num_numbers = input("How many numbers would you like?\n> ")
        if num_numbers.strip():
            break
        else:
            print("Please enter a valid number of numbers.")

    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

    # list of symbols
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    # list of numbers
    numbers = [str(i) for i in range(10)]

    # create a list of characters
    characters = letters[:int(num_letters)] + symbols[:int(num_symbols)] + numbers[:int(num_numbers)]

    # shuffle the characters
    random.shuffle(characters)

    # create a password
    password = "".join(characters)

    # print the password
    print(f"Your password is: {password}")

    # ask if user wants to generate another password
    another_password = input("Do you want to generate another password? Type 'yes' or 'no'.\n> ").lower()

    if another_password == "no":
        break
    else:
        continue