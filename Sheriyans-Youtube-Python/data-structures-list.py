# DATA STRUCTURES LIST, SET, TUPPLE, DICTIONARY
# The other way you can do indexing without the for loops are using core indexing.
# This is also called list indexing and slicing.
a = [12,34,32,43,45,53,54,5,4,322]
print(a[0:5:1])
print(a[len(a):4:-1])

# # In this we are looping on the list using the indexing and giving us the value
a = [12,34,32,43,45,53,54,5,4,322]
for i in range(0,len(a)-1,1):
    print(a[i])
    # for i in a:
    # print(i) so in this way we can iterate over the list
    
a = [12,34,32,43,45,53,54,5,4,322]
for i in range(0,len(a)-1,1):
    print(i) # this will give us the index number on each iterations. However, this is possible by using the range function.
 
a = [12,34,32,43,45,53,54,5,4,322]
for i in a:
    print(i) # this will give us the values directly without indexing. So over here we are directly accessing the vlaue not indexes. So we are traversing without the indexs.
    
# What is the methods and what are the lists methods?
How to the check the methods of the list
print(dir(list))

help(list) # by running this you can see the functions and modules to see with the list
 
a = ["apples", "oranges", "mango", "banana"]
a.append(47)        # Append also put it in the last of the indexth value.
a.append("orange2")
a.append(print())
a.insert(1,2) # Insert will always always in the middle or in the order. 1 --> it is the first index and 2 is the value to be put in the list of the first indexth.
a.extend([7,100,500]) 
a.remove(47)
a.remove(2)
print(a)
a.index()

for i in a:

    print(i) # this will give us the values directly without indexing. So over here we are directly accessing the vlaue not indexes. So we are traversing without the indexs.
# question 1
a[0] = 10
print(a)

l = [1,-53,67,45,3533,-7676,332,-55]
print("Positive elemets are")
for i in l:
    if i >= 0:
        print(i)
print("Negative elements are")
for i in l:
    if i <= 0:
        print(i)


# Question 2? Print he mean (Average of the list element)
l = [12,435,43,545,34234,6,34]
sum = 0
for i in l:
    sum = sum + i

print(round(sum/len(l))) # The reason we used the len(l) because we want the average and average is total of the value / number of values.

l = [12,36,14,19,568,6,13,128,]
largest = l[0]
index = 0
for i in range(0,len(l),1):
    if l[i] > largest:
        largest = l[i]
        index = i
        print(i)
        print(largest)
print(f"Your largest number is {largest} at the index {index}")

It is the same question but solved little bit differrently.

l = [12,36,14,19,568,6,13,128,]
largest = l[0]
index = 0
for i in range(0,len(l),1):
    print(i)
    if l[i] > largest:
        largest = l[i]
        index = i
        print(largest)
        print(index)
print(f"Your largest number is {largest} at the index {index}")

## Question print the largest and the second largest variables?

l = [2500, 45,342,2454,5534,34,23,6,565,23,43,234,2345,22,12,234,2,32]
largest = 0
sec_largest = 0
index = 0
for i in l:
    # print(i)
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i
      

print(largest)
print(sec_largest)

l = [12,16,18,19,22,12,33,1.5,32]
largest = l[0]
sec_largest = l[0]
for i in l:
    print(i) # Do remember that i will iterate over all the values of the list.
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest: # We all know that i will iterate over all the values of the list in anycase. So we will check if the if i is greater than second_largest than reassign the second_larget in i
        sec_largest = i
print(f"first largest is {largest} the seocnd largest is {sec_largest}")

# Question to check if the list is sorted or not.

a = [12,13,14,15,16]
for i in range(len(a)-1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("Your list is not sorted")
        break 
else:
    print("Your list is sorted")


