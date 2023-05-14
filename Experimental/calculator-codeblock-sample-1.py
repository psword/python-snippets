# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 06:48:41 2022

@author: philipsword
"""

#let's define the function 'calculator'
def calculator(x, y, answer):
    #set the output back to zero
    operation = 0
    #set the operation and substitute variables in the function
    if answer == "multiply":
        operation = x*y
        print("Here is the operation we are performing: x*y")
        print("Here is the result from the calculation you have performed: "+str(operation))
    elif answer == "divide":
        operation = x/y
        print("Here is the operation we are performing: x/y")
        print("Here is the result from the calculation you have performed: "+str(operation))
    elif answer == "subtract":
        operation = x-y
        print("Here is the operation we are performing: x-y")
        print("Here is the result from the calculation you have performed: "+str(operation))
    elif answer == "add":
        operation = x+y
        print("Here is the operation we are performing: x+y")
        print("Here is the result from the calculation you have performed: "+str(operation))

#we set initial values for x and y here
x = 0
y = 0
answer = 0
#user input received below
print("This is a simple calculator. It can add, subtract, multiply, or divide.\n")
print("Please choose from this list: multiply, divide, add, subtract.")
#logic check - must match te list
while answer not in {"multiply", "divide", "add", "subtract"}:
    answer = input("Enter the operation would you like to perform?\n")
#logic check for the variables - must be integers
while True:
     try:
         x = int(input("Please choose a number for your first variable: \n"))
     except ValueError:
         print("\nYou must type a valid integer!  Try again.\n")
     else:
         break
while True:
     try:
         y = int(input("Please choose a number for your second variable: \n"))
     except ValueError:
         print("\nYou must type a valid integer!  Try again.\n")
     else:
         break

#run the function one time
calculator(x, y, answer)