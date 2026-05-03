set = {1,2,3,4,5,5,5,5}
print(set)
print(len(set))

set.add(6)
print(set)

set.remove(3)
print(set)

# set.clear()
# print(set)

set2 = {7,8,2,3,9}
print(set.union(set2))

print(set.intersection(set2))