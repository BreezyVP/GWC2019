#imports the ability to get a random number (we will learn more about this later!)
from random import *
#Generates a random integer.
aRandomNumber = randint(1, 20)
guesses = 3
# For Testing: print(aRandomNumber)
while guesses < 0:
      guess = input("Guess a number between 1 and 20 (inclusive): ")
      if not guess.isnumeric(): # checks if a string is only digits 0 to 9
            print("That's not a positive whole number, try again!")
        else:
            guess = int(guess) # converts a string to an integer
        if guess == aRandomNumber:
            print ("Congrats! You got it!")
            break
        elif guess > aRandomNumber:
            print ("Too high! Try again.")
        else:
            print ("Too low! Try again.")
    guesess -= 1
        if guesses == 0:
            print ("Sorry, but the number was" + str(aRandomNumber))
