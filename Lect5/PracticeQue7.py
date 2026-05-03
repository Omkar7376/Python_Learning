#1. print elemnts from the list [1,4,9,16,25,36,49,64,81,100] 

list = [1,4,9,16,25,36,49,64,81,100]

for val in list:
    print(val)

#2. search number x from tuple (1,2,3,4,5,6,7,8,9,10)

tuple = (1,2,3,4,5,6,7,8,9,10)
print(tuple)

x = int(input("Choose number from tuple to search : "))

idx = 0
for val in tuple:
    if x == val:
        print("value found at idx : ", idx)
    else:
        print("value not found")
    idx += 1