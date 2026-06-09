set = {1,2,3,4}
print(set)
print(len(set))

set.add(6)
print(set)

set.remove(3)
print(set)

# set.clear()
# print(set)

set2 = {3,4,5,6}
print("\n",set.union(set2))

print("\n",set.intersection(set2))

print("\n",set.difference(set2))

print("\n",set.symmetric_difference(set2))