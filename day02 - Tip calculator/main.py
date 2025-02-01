# Tip Calculator

print("Welcome to the tip claculator")

# ask for total bill
while True:
    total_bill = input("What was the total bill?\n> ")
    if total_bill.strip():
        break
    else:
        print("Please enter a valid bill amount.")

# ask for tip percentage
while True:
    tip_percentage = input("What percentage tip would you like to give ?")
    if tip_percentage.strip():
        break
    else:
        print("Please enter a valid tip percentage.")

# ask for number of people
while True:
    num_people = input("How many people to split the bill?\n> ")
    if num_people.strip():
        break
    else:
        print("Please enter a valid number of people.")

# calculate tip amount
tip_amount = (float(total_bill) * float(tip_percentage)) / 100 

# calculate total bill with tip 
total_bill_with_tip = float(total_bill) + tip_amount

# calculate bill per person
bill_per_person = total_bill_with_tip / int(num_people)

# Printing bill per person using f-string
print(f"Each person should pay: {bill_per_person:.2f}")
