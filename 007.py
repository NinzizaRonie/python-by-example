"""
Ask the user for their name and their age. Add 1 to their age 
and display the output [Name] next birthday you 
will be [new age]. 
"""
name = input("What is your name: ")
age = int(input("How old are you: "))
newage = age + 1
print(name, "next birthday you will be ", newage)