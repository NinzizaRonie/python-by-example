"""
Ask for two numbers. If 
the first one is larger 
than the second, display 
the second number first 
and then the first 
number, otherwise show 
the first number first and 
then the second. 
"""
first = int(input("Please enter any number: "))
second = int(input("Please enter any number: "))

if first > second:
    print(second , first)
else:
        print(first , second)