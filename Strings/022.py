"""
Ask the user to enter their first name and surname in lower 
case. Change the case to title case and join them together. 
Display the finished result. 
"""
firstname = input("please enter your first name in lower case: ")
surname = input("please enter your surname in lower case: ")
firstname = firstname.title()
surname = surname.title()
name = firstname + " " +surname
print(name)