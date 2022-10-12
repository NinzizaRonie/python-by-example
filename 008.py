"""
Ask for the total price of the bill, then ask how 
many diners there are. Divide the total bill by the 
number of diners and show how much each 
person must pay. 
"""
total = int(input("What is the total bill? "))
dinnernum = int(input("How many dinners were there? "))
billofeach = total / dinnernum 
print("Each person must pay", billofeach, ".")