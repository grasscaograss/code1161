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