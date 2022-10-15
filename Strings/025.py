"""
Ask the user to enter their first name. If the length 
of their first name is under five characters, ask 
them to enter their surname and join them 
together (without a space) and display the name 
in upper case. If the length of the first name is five
or more characters, display their first name in 
lower case. 
"""
name = input("please enter your first name: ")
# longer method.
#length = len(name)
#if length < 5:

if len(name) < 5:
    surname = input("please enter your surname: ")
    name = name + surname
    name = name.upper()
    print(name)
else:
    print(name.lower())