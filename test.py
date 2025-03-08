while True:
    try:
        num1 = float(input("Enter your first number "))
        break
    except ValueError:
        print("Please enter valid numbers only ")


        
while True:
    print("\nOpration : + , - , * , /")
    calc = input("Enter your oprator: ").strip()

    while True:
        try:
            num2 = float(input("Enter your second number "))
            break
        except ValueError:
            print("Please enter valid numbers only ")


    if calc == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif calc == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif calc == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif calc == "/":
        if num2 == 0:
            print("it can not divide by 0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("invalid opration")
