#1. take input from user and store it in a list (movie name)

movie = []
mov1 = input("Enter movies name  1 : ")
mov2 = input("Enter movies name  2 : ")
mov3 = input("Enter movies name  3 : ")

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)

print(movie)

#2. check list contains palimdrom of element

list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("List is palimdrom")
else:
    print("List is not palimdrom")

#3. count number of students with grade A in a tuple

grades = ('A', 'B', 'C', 'A', 'D', 'A', 'B')
count_A = grades.count('A')
print("Number of students with grade A:", count_A)

#4. create a list of 5 character and sort it in ascending order
characters = ['d', 'a', 'e', 'b', 'c']
characters.sort()
print(characters)