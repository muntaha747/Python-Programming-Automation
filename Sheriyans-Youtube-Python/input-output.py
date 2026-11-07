# Input and output are done
#output is only done with the print functions only
name = "akarsh"
age = "23"

print(name)
print(age)
print(name,age)

# Raw String and Formatted string
print("hello my name is ", name, "and my age is", age) # --> without formatted and raw string.
print(f"My name is {name} and my age is {age}") # --> Formatted string.

# Input functions --> Always we have to store the input in the variables because without storing in the variables we cannot store the input.
name = input("hello what is your name")
age = input(f"Hello {name} how old are you")
print(f"Hello {name} How are you doing today?")
print(type(int(age))) # We converted data type from str to int because anything inside the input is string not integer even though the age is number but still it is an string without type conversion.

