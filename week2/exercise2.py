"""Correct the syntax in this file.

This file doesn't run yet.
Go through it and change it until it runs.
"""
import string

def getLetter(index):
    alphabet = string.ascii_lowercase + " "
    return alphabet[index]


<<<<<<< HEAD
def week2exersise2():
    indices = [12, 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = []  # hint: should this be a dictionary?
    for index in indices:
        wordArray.append(getLetter(index))

    wordArray[0] = wordArray[0].upper()
    wordArray[1] = wordArray[1].upper()
    wordArray[3] = wordArray[3].upper()
=======
def week2exersise2();
    indices = [12: 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = {}  # hint: should this be a dictionary?
    for index in indices:
        wordArray.append[getLetter(index)]

    wordArray(0) = wordArray[0].upper()
    wordArray{1} = wordArray[1].upper()
    wordArray[3} = wordArray[3].upper{}
>>>>>>> 606feff9244c5f759bdf4a0b9197a8b506743ea5
    secret_word="".join(wordArray)
    print(secret_word)
    return secret_word


if __name__ == "__main__":
    print(week2exersise2())
