# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a basic calculator function.  Second version.

Basics of code by Farhan Anjum.  Orginal options werw #1-4.
Code modded by Farhan, Denis, and Philip.

"""
# Added by psword//import math for sqrt function
from math import sqrt

# Add, subtract, multiply, divide//Farhan
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Squareroot and square//psword
def squareroot(x):
    return sqrt(x)

def square(x):
    return x ** 2




# Restructured "while true" loop and added logic checks for valid numeric input//psword
while True:
    
    print("-----------------------\n-----------------------")
    print("\nSelect operation.\n")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    # 5 added by psword
    print("5.Square Root")
    # 6 added by psword
    print("6.Square")
    # 7 added by psword
    print("7.Exit")
    print("\n-----------------------\n-----------------------")
    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    # Check for a valid choice//psword
    while choice not in {'1', '2', '3', '4', '5', '6', '7'}:
        print("I think you selected something not listed as a valid operation.")
        print("Enter the operation would you like to perform?\n")
        choice = input("(1/2/3/4/5/6/7):")
        
    # Basic code to input the choice for add, subtract, multiply, divide//Farhan
    # Added logic checks for correct numeric input [no letters]
    if choice in ('1', '2', '3', '4'):
        while True:
             try:
                 num1 = float(input("Enter first number: "))
             except ValueError:
                 print("\nYou must type a valid number!  Try again.\n")
             else:
                 break
        while True:
             try:
                 num2 = float(input("Enter second number: "))
             except ValueError:
                 print("\nYou must type a valid number!  Try again.\n")
             else:
                 break    
    # Code to import number for square root//psword
    if choice in ('5'):
        while True:
             try:
                 num1 = float(input("Enter the number for the square root function: "))
             except ValueError:
                 print("\nYou must type a valid number!  Try again.\n")
             else:
                 break
    # Code for input number for square//psword         
    if choice in ('6'):    
        while True:
             try:
                 num1 = float(input("Enter the number to square: "))
             except ValueError:
                 print("\nYou must type a valid number!  Try again.\n")
             else:
                 break
        
    # Additional code block for the exit choice//psword            
    if choice in ('7'):
        print("Exiting!")
        break
    
    # Enter the operations for each choice      
    if choice == '1':
        print("Here is your result: \n\nOutput:", num1, "+", num2, "=", add(num1, num2), '\n')

    elif choice == '2':
        print("Here is your result: \n\nOutput:", num1, "-", num2, "=", subtract(num1, num2), '\n')

    elif choice == '3':
        print("Here is your result: \n\nOutput:", num1, "*", num2, "=", multiply(num1, num2), '\n')

    elif choice == '4':
            print("Here is your result: \n\nOutput:", num1, "/", num2, "=", divide(num1, num2), '\n')
            
    # Additional if added by psword for sqrt
    if choice == '5':
        print("Here is your result: \n\nThe square root of ", num1, "=", squareroot(num1), '\n')
    # Additional if added by psword for square
    if choice == '6':
        print("Here is your result: \n\nThe square of ", num1, "=", square(num1), '\n')
    
        
