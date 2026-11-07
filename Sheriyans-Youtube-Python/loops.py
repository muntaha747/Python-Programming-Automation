# For Loops
range(0,20,1) # --> (Start,Stop,Steps) this is the range fucntion.
# Question 1
a = range(1,21,1)
for i in a:
    print(i)
for i in range(20,50,1):
    print(i)
for i in range(50,20,-1):
    print(i)
for i in range(-1,-16,-1):
    print(i)
for i in range (5,51,5):
    print(i)
n = int(input("Which table you want"))
for i in range(n,n*10+1,n):
        print(i)


# Using for loops over string
a = "SHERIYANS"
for i in range(0,9,1):
    print(a[i])
a = "SHERIYANS"
for i in range(len(a)):
    print(a[i])
a = str("SHERIYANS")
for i in a:
    print(i)
    
Continue and Break statement in loops

for i in range(1,21,1):
    if i == 9:
        continue
    else:
        print(i)
    
# Question 1?
n = int(input("Please tell me your number?\n"))
for i in range(n):
    print("hello world")
    
# Question 2?
n = int(input("Please tell me your number?\n"))
for i in range(1,n+1,1):
    print(i)

# Question 3?
n = int(input("Please tell me your number?\n"))
for i in range(n,0,-1):
    print(i)

# Question 4?
n = int(input("Please tell me your number?\n"))
for i in range(1,11): 
    print(f"{n} x {i} = {n*i}")
    
Question 5/
a = 10
a = a + 5
print(a)
n = int(input("Enter a number for sum"))
sum = 0
for i in range(1,n+1):
   sum = sum + i
   print(sum)
print(f"{sum} is the total")

# Question 6 --> We want the factorial of the number which is given in the input?
n = int(input("Please tell me your number?\n"))
sum = 1
for i in range(1,n+1):
    sum *= i
    print(sum)

# Question 7 --> In this question we will be using for loops, ifelse and compounding
n = int(input("Please tell me your number?\n"))
even = 0
odd = 0
if n % 2 == 0:
    print("it is the even number")
    for i in range(1,n+1,1):
        even += i
        print(even)
    print(f"The total Number of Even number is {even}")
else:
    print("it is the odd number")
    for i in range(1,n+1,1):
        odd += i
        print(odd)
    print(f"The sum of total odd number is {odd}")
print(f"The sum of total odd number is {odd} and the total sum of even number is {even}")
 
 
 # Question 8 Print all the numbers of the factor
n = int(input("Please tell me your number?\n"))
for i in range(1,n+1):
    if n % i == 0:
        print(i)


 # Question 9 Print all the numbers of the factor and sum all of it (The perfect number is only 6, 28 and very few number)
n = int(input("Please tell me your number? "))
sum = 0
for i in range(1,n,1): #--> The reason we didn't do n+1 because we want perfect number and perfect number means you cannot count the number which you for addition than only it becomes perfect number
    if n % i == 0:
        print(i)
        sum += i
print(f"The total sum of the factors of your number is {sum}")
if sum == n:
    print("Your number is perfect")
else:
    print("Your number is not perfect")

# Question 10 get me the factors of the number and count it?
n = int(input("Please tell me your number? "))
count = 0
for i in range(1,n+1,1):
    if n % i == 0:
        print(i)
        count += 1
print(count)
if count == 2:
    print("The number is prime")
else:
    print("The number is not prime")

# Question 11?
a = "SHERIYANS"
b = ""
for i in range(len(a),-1,-1):
    b += a[i]
print(b)    

# Question 12?
str1 = "P@#yn26at^&i5ve"
char = 0
Digits = 0
Symbols = 0

for i in str1:
    if i.isalpha(): #this is the function which will check if the character is alphabet or not
        char += 1
        print(f"{i} a character is found")
    elif i.isdigit(): #this is the function which will check if the character is digit or not
        Digits += 1
        print(f"{i} a digit is found")  
    else:   
        Symbols += 1 # There is not fucntion for symbols so we will just use else statement to count the symbols
        print(f"{i} a symbol is found")
print(f"The total number of characters is {char}")
print(f"The total number of Digits is {Digits}")
print(f"The total number of Symbols is {Symbols}")

WHILE LOOPS
a = 1
while a <= 29:
    a += 1
    print(a)

## Question 1? Separate each digits of the number
a = int(input("Enter a Number that you want to run in a while loop and get a separation of a number"))
while a > 0: 
        print(a % 10) 
        a //= 10
        
Question 2?
a = int(input("Enter a Number that you want to run in a while loop and get a separation of a number"))
b = 0
while a > 0:
    last_digit = a % 10
    b = (b * 10) + last_digit
    a = a // 10
print(f"The Total number for the variable b is {b}")

# Question 3?
a = int(input("Enter a Number that you want to run in a while loop and get a separation of a number"))
a2 = a
b = 0
while a > 0:
    last_digit = a % 10
    b = (b * 10) + last_digit
    a = a // 10
print(f"The Total number for the variable b is {b}")
if a2 == b:
    print("it is a pallidrome")
else:
    print("It is not a pallidrome")
    