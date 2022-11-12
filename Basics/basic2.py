# Range elaboration

# range also comes with a third parameter
# that is a incrementer or step value

for i in range(0,10,2):
    print(i) # it prints numbers after every 2 step

# thus with the use of this we can decrement also
# while providing first para > second para
for i in range(10,0,-2):
    print(i,end=" ")
# a range is not equivalent to list according to python3
# but
print(list(range(0,10))) # to convert range to list


# More about lists

list = [1,2,3,4]
list2 = list
list = list +[7]

# since we know that on concatenation a new list 
# is formed leaving the old list we old values on addition
# of another value to it.
print(list)
print(list2)

# to prevent this behaviour or refer to same object
# we can use append method with a list

list2 = list
list.append(8)
print(list)
print(list2)

# Note append takes only one parameter so if we want 
# to append a full another list to one we have we can't do it


# Therefore we have extend
# An extend takes a list as an argument to add two list

list.extend(list2) # list = list + list2
print(list)


# to remove first occurence of any element in list
# we use remove method with the list object

# list.remove(10) # if value doesn't exits it will throw error(value error)

list.remove(7)
print(list) # only first occurence will be deleted of 7
list.remove(7)
print(list)
# list.remove(7)
# print(list) # no occurence left

# Based on values given to slice of lists
# it can either shrink to expand 

ls1 = [1,2,3,4]
print(ls1)
ls1[2:] = [9,10]
print(ls1)
ls1[2:] = [11,12,13]
print(ls1)
ls1[0:2] = [21,22,23]
print(ls1)

# so be careful before updating list2

# in command used to find whether a element is present in list
print(21 in ls1)

# we can use in to repeadtly remove common elements
# with remove

temp_list = [1,2,3,4,1,3]
x = 3
while x in temp_list:
    temp_list.remove(x)
print(temp_list)


# some of the common list methods

temp_list_2 = [1,44,3,14,25]
temp_list_2.reverse()
print(temp_list_2)
temp_list_2.sort()
print(temp_list_2)
print(temp_list_2.index(3)) # if value is not found it will throw an error



