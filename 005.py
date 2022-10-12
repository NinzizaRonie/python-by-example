"""
Ask the user to enter three 
numbers. Add together the first 
two numbers and then multiply 
this total by the third. Display the 
answer as The answer is 
[answer]. 
"""

number1 = int(input("Please enter your first number:"))
number2 = int(input("Please enter your second number:"))
number3 = int(input("Please enter your third number:"))
answer = (number1 + number2) * number3
print("The answer is", answer)

