import calculator_functions as calculator

def main():
    print("Welcome to the Calculator App")

    while True:
        num1 = calculator.get_valid_number("Enter first number: ")
        num2 = calculator.get_valid_number("Enter second number: ")
        operator = input("Choose operation ( +, -, *, /): ").strip()
        print(f"Result: {calculator.perform_calculattion(num1, num2, operator)}")
        if input("Calculate again? (yes/no): ").strip().lower() != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main() 