# mutable types in python
# have global scope by default
# means they can be accessed by any function
# any time and updation or deletion will
# be reflected

# example

dict1 = {
    "Hello":1
}
print(dict1)
def add_dict_value(value1,value2):
    dict1[value1] = value2 # we can acesss and modify

add_dict_value("Bru",3) 
print(dict1) #value are added

# on the other hand by default immutable 
# type have local scope means modification 
# will not be reflected

# def f():
#     y = x
#     print(y)
#     x = 22 # we modified but no change at result
# x = 7 # outside scope is changed
# print(x)

# to make a global name inside function we
# use functions

def f():
    global x
    y = x
    print(y)
    x = 22
x = 7
f()
print(x)