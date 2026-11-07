# VARIABLES
Age = 12
Name = "Muntaha"
print (Age)
sher = "harsh_bhaiya"
print (sher)

# You should not start numbers 1 in variables name
# You cannot use special characters in the variables *&@# except _

SheriyansSchool = "students" # This is called pascal case
sheriyansSchool = "students" # This is camel case in which starting of the letter is lowercase.
sheriyans_school = "students" # This is snake case

# variables stores the differrent types.

#  Data Types (String, Integer, float(Decimal number), complex, Boolean)

# Integer
a = 12 
print (type(a))

# Float
b = 58.6
c = 12/3
print(type(b))
print(type(c))

# Complex Number
v = 34j # j is the imaginary 
print(type(v))
 
# Strings
f = "Muntaha"
print(type(f))
e = "Muntaha"
print(type(e))

# Boolean
t = True
f = False
print(type(t))

# strings and type conversion
a = 12 # this is int
b = "N"
print(ord(b)) # A is the uni code and strings saves the uni code of the characters and will take the space.
n = 78
print(chr(n))

# Indexing and its access and indexing starts at 01234 --> munta--> this is called positive indexing. ahat -1, -2, -3, -4 muntaha from last to middle than it is negativve indexing.
a = "hello brother"
print(a[1:3])
print(a[0:10])
print(a[0])
print(a[0:-4])


# String slicing a[start:stop:steps] [0:stop + 1:1]--> this is by default and space is also count as an index. Also a[0::1] in middle we havent given anything which means in middle we want to go to the end of the string indexes.
a = "Muntaha Coder"
print(a[0:7:1])

# Type Conversion of the Data Types string to int and int to float and float to string. These are type conversion functions ().
# Print() are also functions like int(), str(), float(), bool()
a = 12
# or
a = str(a)
print(type(a))
print(type(str(a)))

a = "12"
a = int(a)
print(type(a))


