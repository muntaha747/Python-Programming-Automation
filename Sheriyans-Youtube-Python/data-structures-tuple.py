#TUPLE  # Tuples are immutable. They are not mutable list list(You cannot change the value of the tuples), Duplicates values are allowed in tuple like list, ordered and access the values with the indexes,
#Tuple are hetrogenous like list (Means you can write multiple data types.)
#Tuple are traveresed as the same manner as list like for loop and also access with values or indexth values.
a = (1,2,3,4,5,6)
print(type(a))

for i in range(0,len(a),1):
    print(a[i])

index = a.index(5)
print(index)
count = a.count(6)
print(count)

a,b,c,d = (1,2,3,4) # tuple unpacking

print(a)