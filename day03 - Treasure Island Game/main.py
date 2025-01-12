# Treasure Island Game

#print a treasure schematic
print(''' 
*******************************************************************************
          |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    *|                   |  ,-"_,=""     `"=.|                  |

    *|___________________|__"=._o`"-._        `"=.______________|_______


*******************************************************************************
      ²
    ''')

direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n> ").lower()

if direction == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n> ").lower()
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n> ").lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")

