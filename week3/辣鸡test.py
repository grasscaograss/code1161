import random
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
print ("You got it!")