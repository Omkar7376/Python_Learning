str1 = "Hello "
str2 = "omkar"

#Concatenation
print(str1 + str2)

#Length
print(len(str2))

#Indexing
print(str1[1])

#Slicing
print(str2[2:4]) #ka
print(str2[:4]) #omka
print(str2[2:]) #kar

#Nagative Slicing
print(str2[-3:-1]) #ka

#String Functions
print(str2.endswith("ar")) #True
print(str2.capitalize()) 
print(str1.replace("Hello", "Hi"))
print(str2.find("k"))
print(str1.count("l"))