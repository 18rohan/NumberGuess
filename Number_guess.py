import random
import numpy as np
number = random.randint(1,9)


#Number of chances is limited to 5. If a user exhausts all the chances then the game is Over!!
chance = 0

while chance < 5:
    #Taking an input from a user
    guess = int(input("Enter a number: "))
    types = type(guess)
    if type(guess) != types:
        print("Wrong Input")
    else:
        if guess == number:
            print("CONGRATULATIONS.YOU WON!!")
            break
        elif guess < number:
            print("The number you entered is too low. Try a number higher than",guess)
        elif guess > number:
            print("The number you entered is too high. Try a number lower than",guess)
    chance += 1
if not chance < 5:
    print("YOU LOST!!")
