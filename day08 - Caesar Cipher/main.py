# Caesar Cipher : Shifted letters encryption

def encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            if char.isupper():
                new_char = new_char.upper()
            encoded_message += new_char
        else:
            encoded_message += char
    return encoded_message

def decode(message, shift):
    return encode(message, -shift)

while True:
    # Ask user encode or decode
    operation = input("Please enter 'encode' to encrypt or 'decode' to decrypt:>").lower()
    
    if operation not in ["encode", "decode"]:
        print("Invalid input. Please enter 'encode' or 'decode'.")
        continue

    # Ask user a message
    message = input("Enter your message:>")

    # Ask user the desired shift
    while True:
        try:
            desired_shift = int(input("Enter the shift value:>"))
            break
        except ValueError:
            print("Please enter a valid integer for shift value.")
    
    # Do the operation
    if operation == "encode":
        result = encode(message, desired_shift)
    elif operation == "decode":
        result = decode(message, desired_shift)
    
    # Print the result
    print(f"Result: {result}")
    
    # Ask user if they want to continue
    continue_choice = input("Do you want to continue? (yes/no):>").lower()
    if continue_choice != "yes":
        break