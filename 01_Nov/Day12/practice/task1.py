#!/usr/bin/env python3
#task1

#accept 2 number input values from user



try:
    input_1 = int(input("Please enter a numeric value:"))
    input_2 = int(input("please enter a numeric value:"))

    result=input_1/input_2

except ZeroDivisionError:
    print ("Error: cannot divide by zero!!🥲")
    print ("Script continues after handling exception")

except TypeError:
    print ("The data entered is not a number")

except ValueError:
    print ("please Enter a number")
