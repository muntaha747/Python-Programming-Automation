print() # This is inbuilt function 
() # this is how you call the function.
# print("hello how are you")
#def # this is user defined function
def hello():
    print("This is a hello function so i am doing hello")
hello()

# These are called positional parameters and arguements
def sum(a,b): # These a,b are called postional arguements.
    print(f"The sum of the paramters is {a+b}")
sum(12,12)
sum(45,45)


# Key word Parameters and Arguements
def hello(name, age): # These name, age is the key word arguement
    print(f"your name is {name} and your age is {age}") 
hello(name = "Muntaha", age = 33)  

# Default parameters and arguements.
def sum(a,b=45): # These a,b are called postional arguements.
    print(f"The sum of the paramters is {a+b}")
sum(45,45)

# Question? I will be passing a string to check is it a pallindrome or not?
def pallindrome(str):
    rev = ""
    for i in range (len(str)-1,-1,-1):
        rev = rev + str[i]
    if rev == str:
        print("The string {str} which you proivided is pallindrome")
    else:
        print("The string {str} you provided is not a pallindrome")
            
pallindrome(input("Please enter your string to check weather it is pallindrome or not\n"))