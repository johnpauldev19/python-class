print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random

#  This is a code that helps you guess

number = random.randint(1,2)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 2: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))