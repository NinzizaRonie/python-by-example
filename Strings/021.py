"""
Ask the user to enter their first name and then ask them to 
enter their surname. Join them together with a space between 
and display the name and the length of whole name. 
"""
from distutils.command.build_scripts import first_line_re


firstname = input("please enter your first name: ")
surname = input("please enter your surname: ")
name = firstname + " " +surname
print(name)
length = len(name)
print(length)