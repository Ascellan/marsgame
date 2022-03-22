import random

#tulostetaan toivotus peliin
print("Welcome! This is an exciting game of guessing.")
#assigning the result of input into a variable "guess"
guess = input("Choose a number between 1-10: ")
#generating random number
for i in range(1):
    result = random.randint(1,10)
if result == guess:
    print("That's right!")
else:
    print("Wrong!")
