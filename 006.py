"""
Ask how many slices 
of pizza the user 
started with and ask 
how many slices 
they have eaten. 
Work out how many 
slices they have left 
and display the 
answer in a user friendly format

"""
startnum =int(input("Please enter the total number of pizza slices: "))
takennum = int(input("How many slices of pizza have you eaten? "))
slicesleftnum = startnum - takennum
print("There are", slicesleftnum, "slices of pizza left.")
