# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    list_1=[]
    a=start
    while a< stop:
        list_1.append(a)
        a+=step
    return list_1
        
              


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    list_1=[]
    a=start
    while a< stop:
        list_1.append(a)
        a+=step
    return list_1


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    list_1=[]
    a=start
    while a< stop:
        list_1.append(a)
        a+=2
    return list_1


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    i=  int(input('Enter a number: '))

    while True:
        if i < high and i > low:
            return i
        else:
            i=int(input('Enter again: '))
            continue






def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message= input('Enter a number: ')

    while True:
        try:
            message=int(message)
            return message
        except:
            message=input('Enter a number: ')


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    i= input('Enter a number: ')

    while True:
        try:
            i=int(i)
            if int(i) < high and int(i) > low:
                return i
            else:
                i=input('Enter again: ')
                continue
        except ValueError:
            i=input('Enter again: ')
            continue
    
        
    
  


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
