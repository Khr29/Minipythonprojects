# function to get a valid number
def get_valid_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# function to perform calculations
def perform_calculattion(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2 
    elif operator == "/":
        return "Can not divide by zero." if num2 == 0 else num1/num2
    return "Invalid operation"