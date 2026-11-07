# # DATA STRUCTURES LIST, SET, TUPPLE, DICTIONARY
# # The other way you can do indexing without the for loops are using core indexing.
# # This is also called list indexing and slicing.
# a = [12,34,32,43,45,53,54,5,4,322]
# print(a[0:5:1])
# print(a[len(a):4:-1])

# # # In this we are looping on the list using the indexing and giving us the value
# a = [12,34,32,43,45,53,54,5,4,322]
# for i in range(0,len(a)-1,1):
#     print(a[i])
#     # for i in a:
#     # print(i) so in this way we can iterate over the list
    
# a = [12,34,32,43,45,53,54,5,4,322]
# for i in range(0,len(a)-1,1):
#     print(i) # this will give us the index number on each iterations. However, this is possible by using the range function.
 
# a = [12,34,32,43,45,53,54,5,4,322]
# for i in a:
#     print(i) # this will give us the values directly without indexing. So over here we are directly accessing the vlaue not indexes. So we are traversing without the indexs.
    
# # What is the methods and what are the lists methods?
# How to the check the methods of the list
# print(dir(list))

# help(list) # by running this you can see the functions and modules to see with the list
 
a = ["apples", "oranges", "mango", "banana"]
a.append(47)        # Append also put it in the last of the indexth value.
a.append("orange2")
a.append(print())
a.insert(1,2) # Insert will always always in the middle or in the order. 1 --> it is the first index and 2 is the value to be put in the list of the first indexth.
a.extend([7,100,500]) 
a.remove(47)
print(a)
