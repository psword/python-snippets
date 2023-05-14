# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 23:26:29 2022

@author: philip
"""
class Calculator():
    
    def __init__(self,num1,num2):
        self.input1 = num1
        self.input2 = num2
    
    def add(self):
        return self.input1 + self.input2
    
    def subtract(self):
        return self.input1 - self.input2
    
    def multiply(self):
        return self.input1 * self.input2
    
    def divide(self):
        return self.input1 / self.input2
    
    def nthroot(self):
        return self.input1 ** (1/float(self.input2))
    
    def power(self):
        return self.input1 ** self.input2

choice = "0"

def selection():
    global choice
    print("-----------------------\n-----------------------")
    print("\nSelect operation.\n")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Nth Root")
    print("6.Nth Power")
    print("7.Exit")
    print("\n-----------------------\n-----------------------")
    choice = input(str("Enter choice(1/2/3/4/5/6/7): "))

    while choice not in {'1', '2', '3', '4', '5', '6', '7'}:
        print("I think you selected something not listed as a valid operation.")
        print("Enter the operation would you like to perform?\n")
        choice = input("(1/2/3/4/5/6/7):") 

def entry1():
    global user_entry_1
    while choice != '7':
         try:
             user_entry_1 = float(input("Enter first number: \n"))
         except ValueError:
             print("\nYou must type a valid number!  Try again.\n")
         else:
             break

def entry2():
    global user_entry_2
    while choice != '7':
         try:
             user_entry_2 = float(input("Enter second number: \n"))
         except ValueError:
             print("\nYou must type a valid number!  Try again.\n")
         else:
             break

while True:
    
    selection()
    if choice == '7':
        break
        
    entry1()
    
    entry2()
    
    enter_calculator = Calculator(user_entry_1,user_entry_2)
    
    if choice == '1':
        print("Here is your result: \n\nOutput:", user_entry_1, "+", user_entry_2, "=", enter_calculator.add(), '\n')
    
    elif choice == '2':
        print("Here is your result: \n\nOutput:", user_entry_1, "-", user_entry_2, "=", enter_calculator.subtract(), '\n')

    elif choice == '3':
        print("Here is your result: \n\nOutput:", user_entry_1, "*", user_entry_2, "=", enter_calculator.multiply(), '\n')

    elif choice == '4':
        print("Here is your result: \n\nOutput:", user_entry_1, "/", user_entry_2, "=", enter_calculator.divide(), '\n')

    elif choice == '5':
        print("Here is your result: \n\nOutput:", "the", user_entry_2, "root of", user_entry_1, "=", enter_calculator.nthroot(), '\n')
        
    elif choice == '6':    
        print("Here is your result: \n\nOutput:", "the", user_entry_2, "power of", user_entry_1, "=", enter_calculator.power(), '\n')
    
    else:
        print("Exiting!")
    
    print("Do you want to continue? y/n")
    proceed = input()
    
    while proceed not in {'y', 'n'}:
        print("I think you typed an invalaid input.  Please type y/n.")
        proceed = input()
    
    if proceed == 'n':
        print("Exiting!")
        break
        
if choice == '7':
    print("Exiting!")