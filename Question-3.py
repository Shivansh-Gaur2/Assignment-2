#QUESTION 3
#For a=56 and b=10 with the help of bitwise operators calculate the following:
# A PART
a = 56
b = 10

print("value of a & b:- ",a & b)
# B PART a|b
print("value of a | b:- ",a | b)
# C PART a^b
print("value of a ^ b:- ",a^b)
# D PART Left shift both a and b with 2 bits.
a = a<<2
b = b<<2
print("value of a after shifting left by 2 bits:- ",a)
print("value of b after shifting left by 2 bits:- ",b)

# E PART Right shift a with 2 bits and b with 4 bits.
a = 56
b = 10
a = a>>2
b = b>>4
print("value of a after shifting right by 2 bits:- ",a)
print("value of b after shifting right by 4 bits:- ",b)
