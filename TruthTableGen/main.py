from functions import *

print("Truth Table Generator: ")

while True:
    print("\nUse A-G, & for and, | for or, ! for not, and ()")
    print("To end enter \"quit\"")
    equation = input("Enter boolean equation: ")

    if equation == "quit":
        break


    print(equation)
