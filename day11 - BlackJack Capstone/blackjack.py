# BlackJack Capstone Game

import random

def generate_set():
    """ Generate initial two cards for both player and computer """
    global player_cards, computer_cards
    player_cards = [random.randint(1, 10) for _ in range(2)]
    computer_cards = [random.randint(1, 10) for _ in range(1)]

def generate_player_card():
    """ Generate a random number between 1 and 10 and add to player cards """
    player_cards.append(random.randint(1, 10)) # Just need to extend the list

def generate_computer_card():
    """ Generate a random number between 1 and 10 and add to computer cards """
    computer_cards.append(random.randint(1, 10))

def display_game_set(phase):
    """ Display the current game status based on phase """
    if phase == 1:
        print(f"\nYour cards: {player_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
    elif phase == 2:
        print(f"\nYour final hand: {player_cards}, Total: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, Total: {sum(computer_cards)}")

def search_winner(players_dict):
    """ Determine the winner based on game rules """
    max_score = 0
    winner = None

    for player, data in players_dict.items(): # Often use dict.items() to search in a dict
        card_sum = sum(data["cards"])  # Calculate total card sum

        if card_sum == 21:  # Automatic blackjack win
            return player  
        elif card_sum > 21:
            continue  # continue using example
        else:
            data["score"] = card_sum  # Store valid score
    
    # Find the highest valid score under 21
    for player, data in players_dict.items():
        if data["score"] > max_score and data["score"] <= 21:
            max_score = data["score"]
            winner = player  
    
    return winner  

def blackjack_game():
    """ Main function of the Blackjack game """
    print("\nWelcome to Blackjack Game!")

    while True:
        play_blackjack = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play_blackjack != "y":
            print("Goodbye!")
            break

        generate_set()
        game_phase = 1
        display_game_set(game_phase)

        # Player turn
        while sum(player_cards) < 21:
            another_card = input("\nDo you want another card? Type 'y' or 'n': ").lower()
            if another_card == "y":
                generate_player_card()
                display_game_set(game_phase)
            else:
                break

        # Computer turn (draws until 17 or higher)
        while sum(computer_cards) < 17:
            generate_computer_card()

        game_phase = 2
        display_game_set(game_phase)

        # Determine the winner
        players = {
            "player1": {"cards": player_cards, "score": 0},
            "computer": {"cards": computer_cards, "score": 0},
        }

        winner = search_winner(players)
        if winner == "player1":
            print("\n🎉 You Win! 🎉")
        elif winner == "computer":
            print("\n💻 Computer Wins! 💻")
        else:
            print("\n🤝 It's a Draw! 🤝")

# Run the game
blackjack_game()
