# Band Name Generator

print("Welcome to the Band Name Generator.")

# ask city name
while True:
    city = input("Which city did you grow up in?\n> ")
    if city.strip():
        break
    else:
        print("Please enter a valid city name.")

# ask pet name
while True:
    pet = input("What is the name of a pet?\n> ")
    if pet.strip():
        break
    else:
        print("Please enter a valid pet name.")

# Printing group name using f-string
print(f"Your band name could be {city} {pet}.")