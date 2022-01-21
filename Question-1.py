#QUESTION 1 
#For a given input string “Python is a case sensitive language”. Write python
#code for the following:
# A) Find the length of the input string.

sentence = "Python is a case sensitive language"
print("length of the string is:- ", len(sentence))

#B) Reverse the order of the string in one line code.
print(sentence[::-1])

#C)Using Slice function store “a case sensitive” in new string.
new_str = sentence[10:26]
print(new_str)

#D) Replace “a case sensitive” with “object oriented”.
new_sentence = sentence.replace("a case sensitive", "object oriented")
print(new_sentence) 

#E) Find index of substring “a” in the given input string.
print(sentence.find("a"))

#F) Remove the white spaces from the given input string.
replaced = sentence.replace(" ","")
print(replaced)
