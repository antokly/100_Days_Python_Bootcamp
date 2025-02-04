# Calculator App

import art

print("Welcome to Calculator App!")

def operator_add(a, b):
    return a + b

def operator_substract(a, b):
    return a - b

def operator_multiply(a, b):
    return a * b

def operator_divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

continue_calculation = "n"
num1 = 0

operations = {
    "+": operator_add,
    "-": operator_substract,
    "*": operator_multiply,
    "/": operator_divide,
}

def calculator():
    print(art)
    should_accumulate = True
    num1 = float(input("What's the first number? > "))

    while should_accumulate:
            
        for symbol in operations:
            print(symbol)

        operation_selection = input("Pick an operation: > ")

        num2 = float(input("What's the next number? > "))

        if operation_selection == "+":
            result = operator_add(num1, num2)
        elif operation_selection == "-":
            result = operator_substract(num1, num2)
        elif operation_selection == "*":
            result = operator_multiply(num1, num2)
        elif operation_selection == "/":
            result = operator_divide(num1, num2)
        else:
            print("Invalid operation! Please select a valid operator.")
            continue

        print(f"{num1} {operation_selection} {num2} = {result}")

        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: > ")

        if continue_calculation == "y":
            num1 = result
        elif continue_calculation == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator() #Recursion

calculator()