#1. write a recusrsion func to calculate sum of first n natural numbers

def sum(n):
    if(n == 0):
        return 0
    print(n)
    return sum(n - 1) + n
        
print("sum is :",sum(5))

#2. print elements of list use list, index parameter

list_data = [1,4,9,16,25,36,49,64,81,100]

def list_print(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    list_print(list, idx + 1)

print(list_print(list_data))