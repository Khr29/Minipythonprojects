import random
import time
#define available operators and number range
oprators = ["+","-","*"]
min_operand = 3
max_operand = 12
total_problems = 10
#function to generate a math problem
def genrate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    oprator = random.choice(oprators)

    exp = str(left) +" "+ oprator +" "+str(right)
    answer = eval(exp)
    return exp, answer

#start of the game and game logic
wrong = 0
start_time = time.time()
input("Press enter to start!")
print("---------------------")
for i in range(total_problems):
    exp, answer = genrate_problem()
    while True:
        guess = input("Problem #" + str(i + 1)+": " + exp + " = ")
        if guess == str(answer):
            break
        wrong += 1

#end of game and time calculation
end_time = time.time()
total_time = round(end_time - start_time)
print("---------------------")
print("Nice work!! you finished in ",total_time,"seconds!")