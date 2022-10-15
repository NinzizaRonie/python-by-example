"""
Pig Latin takes the first consonant of a word, 
moves it to the end of the word and adds on an 
“ay”. If a word begins with a vowel you just add 
“way” to the end. For example, pig becomes igpay, 
banana becomes ananabay, and aadvark becomes 
aadvarkway. Create a program that will ask the 
user to enter a word and change it into Pig Latin. 
Make sure the new word is displayed in lower case. 
"""
word = input("Please enter  word: ")

#determine the first letter of the word which is located at index 0.
first = word[0]

#determine the length of the whole word.
length = len(word)
# instruct the word to start from index 1 to the last index number.
rest = word[1:length]
"""
If the first letter is not a vowel,take the first consonant of a word, 
move it to the end of the word and add on an 
“ay”.

"""
if first !="a" and first !="e" and first !="i" and first !="o" and first !="u":
    newword = rest + first + "ay"

#If a word begins with a vowel you just add 
#“way” to the end.
else:
    newword = word + "way"
#print the new word in lower case
print(newword.lower())
