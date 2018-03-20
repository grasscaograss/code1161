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
    if i.isdigit()==True:
        break
    else:
        i=input('Set a lower bound again: ')
        continue
  s=input("Set a higher bound: ")
  while True:
    if s.isdigit()==True:
        while True:
            if int(s)>int(i):
              break
            else:
              s=input("The number should bigger than the low bound, set again: ")
        break
    else:
        s=input('Set a higher bound again: ')
        continue
  print ("Now, guess a number between "+i+" and "+s)
  actualNumber = random.randint(int(i), int(s))
  guessed = False
  while not guessed:
    guessedNumber = input("guess a number: ")
    while True:
        if guessedNumber.isdigit()==True:
            break
        else:
            guessedNumber=input('You should enter a number to guess: ')
            continue
    print("you guessed {},".format(guessedNumber),)
    if int(guessedNumber) == int(actualNumber):
        print("you got it!! It was {}".format(actualNumber))
        guessed = True
    elif int(guessedNumber) < int(actualNumber):
        print("too small, try again ")
    else:
        print("too big, try again   ")  

if __name__ == "__main__":
    advancedGuessingGame()
