#1. Print Length of list
list = [1,2,3,4,5]

def print_len(list_len):
    print(len(list_len))

print_len(list)

#2. print list in a single line 

def print_list(value):
    for i in value:
        print(i, end = " ")
    print("End")

print_list(list)

#3. factorial of n, n is parameter

n = int(input("Enter Number : "))

def fact(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    print(fact)

fact(n)

#4. convert USD to INR

n = int(input("Enter USD Value : "))

def convertor(usd_val):
    inr_val = usd_val * 89
    print(usd_val, "USD = ", inr_val, "INR")

convertor(n)

#5. Print Even or Odd input from user

n = int(input("Enter Number : "))

def print_evenodd(x):
    if(x %2 == 0):
        print("Even")
    else:
        print("Odd")

print_evenodd(n)