
# By default function calls are made
# based on defined argument sequence
# Python gaves feature to swap arguments
# in a function while calling it

def sum_of_two(a,b):
    return a+b

print(sum_of_two(b=5,a=6))

# Default arguments
# just like other language in python
# we can define default arguments if
# we want a default value to load while 
# calling 

def multiple_of_two(a=20,b=40):
    return a*b
print(multiple_of_two())

# inbuilt function like str,int and float
# also have deafult argument like int(value,base=10)
val = int("20",10)
print(val)
val = int("20",8)
print(val)
val = int("A5",16)
print(val)

# we can short the functions using default argument
# but sometimes in recursion based function it may not
# worked as expected say quicksort(arr,l=0,r=len(arr))
# but arr remains same length every recursive call

# while providing default argument it should
# be noted that we should call function based on values
# sequence else it will not assign function that we want

def sum_of_four(a,b,c=10,d=20):
    return a+b+c+d
print(sum_of_four(14,13,99,34))

# Python allows also to use function
# based on conditonal and change their defination
# according to the requirement. 

x= 10
y = 20
if x > y:
    def divide (a=0,b=0):
        return a/b
else:
    def divide(a=0,b=0):
        return b/a
print(divide(x,y))

# we can assign new name to function also
d = sum_of_two
print(d(23,24))
# it can be very useful when making recursive calls

# def sum_times(a,b,d,n):
#     sum = 0
#     for i in range(0,n):
#         sum = d(a,b)
#     return sum
# def multiple(a,b):
#     return a*b
# print(sum_times(12,12,multiple,6))



