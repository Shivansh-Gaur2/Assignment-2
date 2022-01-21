#For any three lengths, there is a simple test to see if it is possible to form a
#triangle. If any of the three lengths is greater than the sum of the other two,
#then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
#converts them to integers, and to check whether the given input lengths can
#form a triangle or not (Print : “Yes” or “No”).

side1 = int(input("Enter length of first side:- ")) 
side2 = int(input("Enter length of second side:- ")) 
side3 = int(input("Enter length of third side:- ")) 

if(side1>=side2+side3 or side2>=side1+side3 or side3>=side1+side2):
    print("No")
else:
    print("Yes")    
    