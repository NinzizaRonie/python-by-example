"""
Task the user to enter a number over 100 and then enter a number under 
10 and tell them how many times the smaller number goes into the larger 
number in a user-friendly format. 
"""
firstnum = int(input("Please enter a number over 100: "))
secondnum = int(input("Please enter a number under 10: "))
times = firstnum // secondnum
print("This second number goes into the first number", times, "times")