# # Conditionals and if-else
a = int(input("Please enter any number"))

if a > 10:
    print("Hello your variable is greater than 10")
    if a == 20:
        print("hey you have entered 20")
elif a < 10:
    print("Hello your variable is lesser than 10")
elif a == 10:
    print("hello you have entered number 10 and it is not fair for our game")
else:
    print("Hey your value is less than 10")


# # Conditionals and if-else
a = int(input("Mummy Please give me the money for Ice-Cream"))

if a == 10:
    print("I will get chocobar ice-cream")
elif a > 10 and a < 20 :
    print("Hi I will have have Mango dolly")
elif a == 30:
    print("I will have cornetto")
else:
    print("Thank you mummy ! I will have family pack")


## Accept two numbers and print the greatest between them

Num_1 = int(input("Enter a Num 1"))
Num_2 = int(input("Enter a Num 2"))

if Num_1 > Num_2:
    print(Num_1)
else:
    print(Num_2)
    

# # Question 2
gender = str(input("Please enter you gender are you male or female"))

if gender == "male":
    print("Good morning sir")
else:
    print("Good morning mam")

# # Question 3
num = int(input("Please Enter a Number"))

if num % 2 == 0:
    print("The Number is Even number")
elif num % 2 != 0:
    print("The number is odd")
else:
    print("It is not a number")
    
# # Question 4
voter_name = str(input("Hey voter what is your name"))
voter_age = int(input("Hey voter what is your age"))

if voter_age >= 18:
    print(f"Hi {voter_name} you are {voter_age} old, so you are eligible for voting")
else:
    print(f"Hi {voter_name} you are less than the permitted age so you are not eligble for voting ")

# # Question 5
year = int(input("Enter a year you want to check is it a leap year or not?\n"))

if year % 400 == 0:
    print("hey your year is leap year")
elif year % 4 == 0:
    print("hey your year is a also a leap year")
else:
    print("Your input year is not a leap year")