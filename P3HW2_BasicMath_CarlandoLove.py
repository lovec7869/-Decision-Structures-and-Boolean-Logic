# Write program Pseudocode(detail algorithm)
# create basic calculator using functions
# CTI-110
# P3HW2 - BasicMath
# Carlando Love
# June 26 2020
#

# program to make simple calculator using functions

def add (x,y):
    """This function add 2 numbers"""
    return x+y
def subtract (x,y):
    """This function subtract 2 numbers"""
    return x-y
def multiply (x,y):
    """This function multiply 2 numbers"""
    return x*y

# take input from user
print ("select operation.")
print ("1.add")
print ("2.subtract")
print ("3.multiply")
print ("4.program will terminate")
choice = input ("Enter choice 1/2/3/4:")

number1 = int (input("enter first number: "))
number2 = int (input("enter second number: "))

if choice == '1':
    print (number1,"+",number2,"=", add(number1,number2))
elif choice == '2':
    print (number1,"-",number2,"=", subtract(number1,number2))
elif choice == '3':
    print (number1,"*",number2,"=", multiply (number1,number2))
elif choice == '4':
    print ("program will terminate.")
    
else:print ("invalid input")
