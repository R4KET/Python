import random
import math

lower_number = int(input("Enter Lower bound:-"))
upper_number = int(input("Enter Upper bound:-"))

x = random.randint(lower_number, upper_number)

print("\n\tYou've only ", 
       round(math.log(upper_number - lower_number + 1, 2)),
      " chances to guess the integer!\n")

#print(x)

count = 0

while count < math.log(upper_number - lower_number + 1, 2):
    count = count + 1

    guess = int(input("Guess a number:-"))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
if count >= math.log(upper_number - lower_number + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")