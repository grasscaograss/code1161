"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
  print ("Welcome to the guessing game!")
  i=input("Set a lower bound: ")
  while True:
    try:
        i= int(i)
        break
    except ValueError:
        i=input('Set a lower bound again: ')
        continue
  s=input("Set a higher bound: ")
  while True:
    try:
        s = int(s)
        while True:
            if int(s)>int(i):
              break
            else:
              s=input("The number should bigger than the low bound, set again: ")
        break
    except ValueError:
        s=input('Set a higher bound again: ')
        continue
  print ("Now, guess a number between "+str(i)+" and "+str(s))
  actualNumber = random.randint(int(i), int(s))
  guessed = False
  while not guessed:
    guessedNumber = input("guess a number: ")
    while True:
        try: 
            guessedNumber=int(guessedNumber)
            break
        except ValueError:
            guessedNumber=input('You should enter a number to guess: ')
            continue
    print("you guessed {},".format(guessedNumber),)
    if int(guessedNumber) == int(actualNumber):
        print("you got it!! It was {}".format(actualNumber))
        guessed = True
    elif int(guessedNumber) < int(actualNumber):
        print("too small, try again ")
    else:
        print("too big, try again  ")  
    return "You got it!"
if __name__ == "__main__":
    advancedGuessingGame()