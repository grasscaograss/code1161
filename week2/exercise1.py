"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
<<<<<<< HEAD
# it makes a list in these words
some_words = ['what', 'does', 'this', 'line', 'do', '?']

for word in some_words: #it will print each words
    print(word)#it printed each words

for x in some_words: #it will print each words
    print(x)#it printed each words

#it will print the list ['what', 'does', 'this', 'line', 'do', '?']
print(some_words)#it printed the list ['what', 'does', 'this', 'line', 'do', '?']

#it will print some_words contains more than 3 words because the object in the list is more than 3
if len(some_words) > 3:
    print('some_words contains more than 3 words')#it printed some_words contains more than 3 words

def usefulFunction(): #it will print the information of  system, node, release, version, machine, and processor.
=======

some_words = ['what', 'does', 'this', 'line', 'do', '?']

for word in some_words:
    print(word)

for x in some_words:
    print(x)

print(some_words)

if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
>>>>>>> 606feff9244c5f759bdf4a0b9197a8b506743ea5
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
<<<<<<< HEAD
    print(platform.uname())#it printed "uname_result(system='Windows', node='Ryzen-1800X', release='10', version='10.0.17115', machine='AMD64', processor='AMD64 Family 23 Model 1 Stepping 1, AuthenticAMD')"
=======
    print(platform.uname())
>>>>>>> 606feff9244c5f759bdf4a0b9197a8b506743ea5

usefulFunction()
