# since we knew we can pass function to a function
# we can create functions that take various arguments
# and updates basisc on function each single value if list

def square(a):
    return a*a

# def square_list_item(s,arr):
#     result = []
#     for i in arr:
#          i = s(i)
#          result.append(i)
#     return result
 
# print(square_list_item(square,list(range(0,10,1))))

# The function above created represents a map function
# built in python that takes arguments as function and list
# and operates the function in each value at list

# the function will work but output 
# is not in form of list but a sequence like range
# so we have to convert it into list

# print(map(square,list(range(2,10))))  
# print(list(map(square,list(range(2,10)))))  


# similarly if we want to filter out values 
# based on conditon from list we use map

# def even(a):
    # return a%2 == 0
# print(list(filter(even,list(range(0,10)))))

# adding both two get square of even number only
# print(list(map(square,filter(even,list(range(0,20))))))

# list comprehnesion we can apply this logics in a list
# syntax itself and get result in from of that

# print([square(i) for i in range(0,10) if even(i)])
#      map         condition             filter

# A small question
# Pythagoras theorem states that sum of square of two sides
# is equal to square of third side which is longer x^2+y^2 =z^2
# calculate all possible value till 100 that satisfies this for x,y,z

# print([(x,y,z) for x in range(100)
#                     for y in range(100)
#                         for z in range(100)
#                             if x^x + y^y == z^z])
# it will generate the values that we need but will also generate
# same sequence repeadtly as well like (3,4,5),(4,5,3),(5,4,3)
# or say n^3 sets more

# to prevent this we can define function only to run for no duplicates

# print([(x,y,z) for x in range(100) for y in range(x,100) for z in range(y,100) if x^x + y^y == z^z])

# generating a matrix using list comprehension

# l = [ [ 0 for i in range(3)] for j in range(4)]
# l[1][1] = 6
# print(l)

print([i for i in range(0,10)])
