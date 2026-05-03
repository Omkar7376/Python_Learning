#1. Print 1 to 100 numbers using while

i = 1
while i<= 100:
    print(i)
    i+=1
print("Stop")

#2. Print 100 to 1 numbers using while
i = 100
while i>= 1:
    print(i)
    i-=1
print("Stop")

#3. print multiplication table of a number n

n = int(input("\nEnter any number : "))
i=1
while i<=10: 
    print(n*i)
    i+=1

#4. print following list using loop [1,4,9,16,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]

i=0
while i< len(num):
    print(num[i])
    i+=1

#5. search for a number x  from the tuple 

num = (1,4,9,16,25,36,49,64,81,100)
print(num)
x = int(input("Choose one value from tuple to search : "))

i = 0
while i<len(num):
    if x == num[i] :
        print("Number fond at inx : ",i)
    else:
        print("not found")
    i+=1
