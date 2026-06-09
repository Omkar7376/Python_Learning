#Read the file
f = open("Lect7/demo.txt", "r")

data = f.read()
line = f.readline()
print(data)
print(line)
f.close()

#Write to the file
# f = open("Lect7/demo.txt", "w")
# f.write("This is new content...")

f = open("Lect7/demo.txt", "a")
f.write("Added Content...")
f.close()