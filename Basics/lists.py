# lists

list = [1,2,3,4,5]
for i in list:
    print(i)

# python list can contain mulitple data at same time
list2 = [True, 3.4, 88,"Hello world"]
for i in list2:
    print(i)

# just like string we can access them using index
# negative as well as positive
print(list2[-3])
# range is also allowed

print(list[:4])
print(list[3:])

# Note a list single index generates a single value at that index
# and a range will generate a sub-list rather than generating a single value
print(list[0]) # 1
print(list[0:1]) # [1]

# nesting of list

list3 = [23,34,[42,44],True,"Hello"]
print(list3[2])
print(list3[2][0])
print(list3[4][2])

# updating list
list3[0] = 88
list3[2][1] = 99
print(list3)

# list are mutable so if we reassign it to another list
# it will change the value at that point/list also

ls = [1,2,3,4]
# print(ls)
# ls2 = ls
# print(ls2)
# ls[1] = 44
# print(ls)
# print(ls2)

# to create copy

ls2 = ls[:]
ls[3] = 'a'
print(ls2)


# on counter to immutable types like int float,bool
# x = 0
# print(x)
# y = x
# print(y) 
# x = 5
# print(x,y)

# Disgression on Equality

arr1 = [1,3,4,5]
arr2 = [1,3,4,5]
arr3 = arr2
print(arr3 == arr2) # == compares value
print(arr3 is arr2) # is compares objects
print(arr1 == arr2)
print(arr1 is arr2)

# concatenation
arr3 =arr1+arr2
print(arr3)
arr1 = arr1 + [8]
print(arr1)
print(arr2 == arr1)