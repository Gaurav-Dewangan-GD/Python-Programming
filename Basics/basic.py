# Print Statement

# print("Hello world")

# Variables

product_ID = 10
product_Price = 3.78
product_Name = "Soda"
print(product_ID,end=" ")
print(product_Price)
print(product_Name)

# Multiple variable assigning

x = y = z = 2
print(x + y +z)

# Data types available 

# Numbers

a = 4 # int
b = 5.5 # float
c = 3.14j # complex
print(c)


# Strings

str1 = "Hello world "
print(str1)
print(str1[0])
print(str1[0:5])
print(str1 * 3)
print(str1[3:-1])

# Lists

stationary_List = ["pencil","book","notebook","eraser"]
stationary_List[0] = "pen"
print(stationary_List)
print(stationary_List[3])
print(stationary_List[2:])

subjects = ["Maths","English"]
print(subjects*3)
print(stationary_List+subjects)

# Tuples

tup_1 = ("Bhilai",2022,5.05,2.3j)
# tup_1[0] = "Durg" doesn't mutate
print(tup_1)
print(tup_1[0])
print(tup_1[0:3])
print(tup_1*2)

# Dictionaries

foods = {
    "fruit":"apple",
    "vegetable":"ladyfinger",
    "meat":"chicken",
    "carb":"cereal"
}
print(foods)

# User input

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# location = input("Enter your location: ")
# print(f'Your name is {name}, you are {age} old and you reside in {location}')

# Data Conversion

# value = int(input("Enter value: "))
# print(value)
# value2 = float(value)
# print(value2)
# value3 = complex(value2)
# print(value3)

# Basic program using conditional

# length = int(input("Enter the length of shape: "))
# width = int(input("Enter the width of shape: "))
# if length == width:
#     print("It's a square!")
# else:
#     print("It's a rectangle")

# print(2**3)
# a = False
# print(int(a))

# if else statements
# price = int(input("Enter the price of commodity: "))
# discount = 0

# functions 
# def discount_rate(percentage):
#     global discount
#     discount = percentage * price
#     print(f'The discount is {discount}')

# if price < 100:
#     discount_rate(0.05)
# elif price < 500:
#     discount_rate(0.1)
# elif price < 100:
#     discount_rate(0.2)
# else:
#     discount_rate(0.25)
# print(f'The final price of commodity is : {price-discount}')


# short program to understand nesting

# num = int(input("Enter the number: "))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print(f'The {num} is divisible by 2 and 3')
#     else:
#         print(f'Divisible by 2 but not 3')
# else:
#     if num%3 == 0:
#         print(f'Divisible by 3 but not 2')
#     else:
#         print(f'Neither Divisible by 2 and 3')

# Loops
# The while Loop

# x = 0
# while( x < 10):
#     x = x+1
#     print(x)

# y = int(input("Enter the number to start countdown: "))
# while( y != 0):
#     print(y)
#     y = y-1

# # while with else
# z = int(input("Enter a number, greater than 3: "))
# while z > 3:
#     print(z)
#     z = z-1
# else:
#     print(f'The count is less than 3')


# the for loop

# for x in range(10):
#     print(x)

# fruits = ["orange","mango","tomato","grapes"]
# for y in  fruits:
#     print(y)

# numbers = [1,2,3,45,49,48,69,37,71,21,31,41]
# for x in numbers:
#     if x%2 == 0:
#         print(f'The list contains even number {x}')
#         break
# else:
#     print("The list doesn't contains even numbers")

# numbers = [3,5,2,7,0,4,3,8,10]
# for num in numbers:
#     if num == 0:
#         pass
#     print("Current Number is : ",num)

# range with parameter

for i in range(0,10,2):
    print(i,end=" ")
print()
def factors(n):
    fl = []
    for i in range(1,n+1):
        if n%i == 0:
            # fl = fl +[i] 
            fl.append(i)
    return(fl)

list2 = factors(10)
print(list2)

def isprime(x):
    return(factors(x) == [1,x])
print(isprime(16))

def update(l,i,v):
    if i>=0 and i < len(l):
        l[i] = v # mutable
        return True
    else:
        v = v+1 # immutable
        return False

ls1 = [1,3,4]
print(ls1)
random = 8
print(random)
status = update(ls1,2,random)
print(status)
print(ls1)
print(random)

# functions structuring
# function should be defined before calling
def f(x):
    return (g(x+1)) # we defined it later but the calling is at last
                    # so it will interperet it top to bottom 
def g(y):
    return(y+3)

z = f(77)
print(z)

# recursion

def fact(x):
    if  x <= 0:
        return 1
    else:
        x *= fact(x-1)
        return x
print(fact(10))