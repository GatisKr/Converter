
# convert.py
#       A program to convert temperature amd distance
# by: GK

import os

def convert():
    ask = input("\nWhat would you like to convert?\nTemperature [1], Distance [2]: ")
    if ask == "1":
        convert_t()
    elif ask == "2":
        convert_d()
    else:
        input("Invalid input. Press <Enter> to quit ")

def convert_t():
    ask = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ")
    if ask.lower() == "c":
        cels()
    elif ask.lower() == "f":
        fahr()
    else:
        input("Invalid input. Press <Enter> to quit ")

def convert_d():
    ask = input("Enter 'K' for Kilometers or 'M' for Miles: ")
    if ask.lower() == "k":
        kilom()
    elif ask.lower() == "m":
        miles()
    else:
        input("Invalid input. Press <Enter> to quit ")

def another_t():
    another = input("\nWould you like another convertion? (Y/N): ")
    if another.lower() in ["y", "yes", "ok"]:
        convert_t()
    elif another.lower() in ["n", "no"]:
        input("Thanks for converting! Press <Enter> to quit ")
    else:
        input("Invalid input. Press <Enter> to quit ")

def another_d():
    another = input("\nWould you like another convertion? (Y/N): ")
    if another.lower() in ["y", "yes", "ok"]:
        convert_d()
    elif another.lower() in ["n", "no"]:
        input("Thanks for converting! Press <Enter> to quit ")
    else:
        input("Invalid input. Press <Enter> to quit ")

def cels():
    try:
        celsius = float(input("\nWhat is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        another_t()
    except (NameError, SyntaxError, ValueError):
        print("Invalid input. Please enter a numeric value")
        cels()

def fahr():
    try:
        fahrenheit = float(input("\nWhat is the Fahrenheit temperature? "))
        celsius = 5/9 * (fahrenheit - 32)
        print("The temperature is", celsius, "degrees Celsius.")
        another_t()
    except (NameError, SyntaxError, ValueError):
        print("Invalid input. Please enter a numeric value")
        fahr()

def kilom():
    try:
        km = float(input("\nEnter distance in kilometers: "))
        ml = km * 0.621371
        print("The distance is", ml, "miles.")
        another_d()
    except (NameError, SyntaxError, ValueError):
        print("Invalid input. Please enter a numeric value")
        kilom()

def miles():
    try:
        ml = float(input("\nEnter distance in miles: "))
        km = ml * 1.60934
        print("The distance is", km, "kilometers.")
        another_d()
    except (NameError, SyntaxError, ValueError):
        print("Invalid input. Please enter a numeric value")
        miles()

def table_fahrenheit():
    celsius = 0
    print("Table for Celsius - Fahrenheit convertion")
    print("-----------------------------------------")
    for i in range(10):
        celsius = celsius + 10
        fahrenheit = 9/5 * celsius + 32
        print(str(celsius) + " C" + " = " + str(fahrenheit) + " F")

os.system("cls")
print("This program converts temperatures and distances.")
convert()
