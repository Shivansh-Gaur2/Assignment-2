#QUESTION 4
#Write a python program to find the greatest of three numbers entered by the user.
num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))
num3 = int(input("Enter the third number:- "))

if(num1>num2):
    if(num1>num3):
        print(f"{num1} is the greatest integer")
    else:
        print(f"{num3} is the greates integer")    
elif(num2>num1):
    if(num2>num3):
        print(f"{num2} is the greatest integer")
    else:
        print(f"{num3} is the greatest integer")