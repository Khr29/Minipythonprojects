import random
print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")
number_to_guess=random.randrange(100)
chances=7
guess_caunter=0
while guess_caunter<chances:
    guess_caunter+=1
    my_guess=int(input("Enter your guess number: "))
    if my_guess==number_to_guess:
        print(f"The number is {number_to_guess} and you found it right in the {guess_caunter} attempt")
        break
    elif guess_caunter>=chances and my_guess != number_to_guess:
        print(f"sorry the number is {number_to_guess}, better luck next time")
    elif my_guess<number_to_guess:
        print("your guess is lesser! ")
    elif my_guess>number_to_guess:
        print("your guess is higher")
        