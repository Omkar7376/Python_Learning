#1. input number and check even or odd

num = int(input("Enter One Number : "))

if(num %2 == 0):
    print("Even")
else:
    print("Odd")

#2. find greater value from 3 numbers from user

a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = int(input("Enter 3rd Number : "))

if(a > b and a > c):
    print("a is grater")

elif(b > a and b > c):
    print("b is grater")

else:
    print("c is grater")