# The Hang Man

import random

word_selected = True
actual_word = ""
win_nbr = 0
lose_nbr = 0

HANGMAN_STAGES = [
    """\n +---+\n     |\n     |\n     |\n    ===\n""",
    """\n +---+\n O   |\n     |\n     |\n    ===\n""",
    """\n +---+\n O   |\n |   |\n     |\n    ===\n""",
    """\n +---+\n O   |\n/|   |\n     |\n    ===\n""",
    """\n +---+\n O   |\n/|\  |\n     |\n    ===\n""",
    """\n +---+\n O   |\n/|\  |\n/    |\n    ===\n""",
    """\n +---+\n O   |\n/|\  |\n/ \  |\n    ===\n"""
]

def word_generator(length):
    """
    Generate a word with the specified length.
    :param length: int
    :return: str
    """
    words = ["python", "hangman", "challenge", "program", "developer", "function", "variable", "coding"]
    filtered_words = [word for word in words if len(word) == length]
    return random.choice(filtered_words) if filtered_words else "test"

def search_in_word(word, letter):
    """
    Search if the letter is in the word.
    :param word: str
    :param letter: str
    :return: bool
    """
    return letter in word

def check_win_or_lose_tour(result, word):
    """
    Check if the player has won or lost the tour.
    :return: bool
    """
    if result:
        print("You found a letter!")
        display_word(word)
        return True
    else:
        print("You missed a letter!")
        display_hangman()
        return False

def actualize_word(selected_word, letter, word):
    """
    Update the word with the found letter.
    :param selected_word: str
    :param letter: str
    :param word: str
    :return: str
    """
    updated_word = ""
    for i in range(len(selected_word)):
        if selected_word[i] == letter:
            updated_word += letter
        else:
            updated_word += word[i]
    return updated_word

def display_word(word):
    """
    Display the word with the found letters.
    :param word: str
    :return: None
    """
    print(" ".join(word))

def display_hangman():
    """
    Display the hangman.
    :return: None
    """
    print(HANGMAN_STAGES[lose_nbr])

def check_win_or_lose_game(selected_word):
    """
    Check if the player has won or lost the game.
    :return: None
    """
    if actual_word == selected_word:
        print("You won! The word was:", selected_word)
        exit(0)
    elif lose_nbr >= len(HANGMAN_STAGES) - 1:
        print("You lost! The word was:", selected_word)
        exit(0)

while True:
    if word_selected:
        # Ask player to select word length / difficulty
        while True:
            word_length = input("Please select the word length (4 to 10 characters):\n> ")
            if word_length.isdigit() and 4 <= int(word_length) <= 10:
                break
            else:
                print("Please enter a valid word length.")

        # Generate word and register it
        selected_word = word_generator(int(word_length))
        actual_word = "_" * len(selected_word)

        word_selected = False

    # Ask player for a letter
    ask_letter = input("Please enter a letter:\n>").lower()

    if len(ask_letter) != 1 or not ask_letter.isalpha():
        print("Please enter a valid single letter.")
        continue

    # Check if the letter exists in the word
    result_tour = search_in_word(selected_word, ask_letter)

    # Update the displayed word
    if result_tour:
        actual_word = actualize_word(selected_word, ask_letter, actual_word)

    # Check win or lose for the round
    if check_win_or_lose_tour(result_tour, actual_word):
        win_nbr += 1
    else:
        lose_nbr += 1

    # Check overall game status
    check_win_or_lose_game(selected_word)