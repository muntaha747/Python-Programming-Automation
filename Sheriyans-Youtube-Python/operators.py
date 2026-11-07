# Operators are arithmetic operators. + - * / %(REMAINDER) // **
a = 5
b = 20
print(a + b)
print(b - a)
print(a * b)
print(b/a)
print(5**4)
print(32%5) # This number is the remainder
# LBODMAS (Bracket Order (Division Multiplication, which ever is left first) Addition Subtraction)

# Assignment operators ( =, ==)
a = 23 
# Compound assignment operations (+=, -=, *=, /=, //=)
a = 20 
# a = 20 + a
a += 20
a += 40
a += 60
print(a)
# Comparision Operators (==, <=, >=) Comparisson operators are always give the results in Boolean True or False.

a = 12.1 
b = 12
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a < b)
print(a > b)
print(ord("A"))
print("Abc" > "B")
# print ("A" > 34) # Can only compare string to string and integer with integer only
print (False > True)

# Logical Operators (There are three types of Logical Operaotors AND, OR, NOT)
print(12 > 20 and 123 > 100 and 34 == 34 and 45 < 90) # and operators says everything should be true, even if one is false and all is true than everything will be false
print (12 > 2 or 2 > 12) # --> Or operations says just give me minimum one true and for false make sure it is all false
print(bool(0))
