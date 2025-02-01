# Secret Auction

def search_max_bidder(bidder_dictionary):
    max_value = 0
    max_bidder = ""
    for bidder, value in bidder_dictionary.items():
        if value > max_value:
            max_value = value
            max_bidder = bidder
    return max_bidder

print("Welcome to the secret auction program.")

# Initialize bid dictionary
bid_dict = {}

others = "yes"

while others.lower() == "yes":
    # Get bidder's name
    bidder_name = input("Enter your name: ")

    # Get bid value and ensure it's a valid integer
    while True:
        try:
            bid_value = int(input("Enter your bid amount: $"))
            if bid_value < 0:
                print("Bid cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    # Store bid in dictionary
    bid_dict[bidder_name] = bid_value

    # Ask if there are more bidders
    others = input("Are there any other bidders? (yes/no): ")

# Determine the highest bidder
max_bidder = search_max_bidder(bid_dict)

print(f"The highest bidder is: {max_bidder} with a bid of ${bid_dict[max_bidder]}")