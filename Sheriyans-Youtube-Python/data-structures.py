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
    
 