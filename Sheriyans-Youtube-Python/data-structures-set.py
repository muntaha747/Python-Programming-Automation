# # SET Data Type
# # Set is mutable like list
# # Set Cannot have duplicates list and tuple
# # Set is not ordered and cannot be accessed with indexes
# # Set is hetrogenous but it cannot store all the data types like but it can store data types like String, numbers, tuples but not everything

# # # s = {1,2,3,4,5,6}
# # # # print(s[0]) --> You cannot call set with the indexes directly.
# # # print(s)

# # # # Hash Functions in the python
# # # b = hash("Hello")
# # # print(b)

# # # s = {1,2,3,4,5,6,7}

# # # for i in s:
# # #     print(i) # You can access set with the values directly rather than indexes.
# # # # for i in range(0,len(s),1):
# # # #     print(s[i])  # --------------> you cannot access the set with the indexth value.

# # # s.remove(2)
# # # s.pop()
# # # s.clear()
# # # print(s)

a = {1,2,3,4,5}
b = {4,5,6,7,8}

# # Union a and b
s = a.union(b) # or you can write like this s = a|b --> pipe symbol.
print(s)
# Intersection 
s = a.intersection(b)  # s = a & b
print(s)

# Differrence
s = a.difference(b) # s = a-b or b-a
print(s)

# Symmetric difference 
s = b^a
print(s)