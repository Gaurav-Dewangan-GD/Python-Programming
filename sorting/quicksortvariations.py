# # using last element as pivot
import random
import math
import statistics
import time
st = time.time()
def partition(ls,first,last):
    pivot = ls[last] # just get last
    left = first 
    right = last-1 # change right to one less than last

    while True:
        while left <= right and ls[left] <= pivot:
            left +=1
        while left <= right and ls[right] >= pivot:
            right -=1
        if left > right:
            break
        else:
            (ls[left],ls[right]) = (ls[right],ls[left])
    (ls[last],ls[left]) = (ls[left],ls[last]) # remember to change pivot to left

    return left

def quicksort(ls,first,last):
    if first < last:
        p = partition(ls,first,last)
        quicksort(ls,first,p-1)
        quicksort(ls,p+1,last)



# using random element

# we use random method in python to chose the random element 
# and then change positon of the element either first or 
# last of list and continue the quick sort technique for first or last

# def partition(ls,first,last):
#     # select one random element 
#     # and swap it with the first one or last
#     rand_element_index = random.choice(range(0,len(ls)))
#       # or rindex = random.randint(first,last)
#     (ls[first],ls[rand_element_index]) = (ls[rand_element_index],ls[first])
#     pivot = ls[first] # just get last
#     left = first+1
#     right = last # change right to one less than last

#     while True:
#         while left <= right and ls[left] <= pivot:
#             left +=1
#         while left <= right and ls[right] >= pivot:
#             right -=1
#         if left > right:
#             break
#         else:
#             (ls[left],ls[right]) = (ls[right],ls[left])
#     (ls[first],ls[right]) = (ls[right],ls[first]) # remember to change pivot to left

#     return right

# def quicksort(ls,first,last):
#     if first < last:
#         p = partition(ls,first,last)
#         quicksort(ls,first,p-1)
#         quicksort(ls,p+1,last)



# selecting median element of first,last, and mid index
# def partition(ls,first,last):
#     mid = (first+last)//2
#     low = ls[first]
#     high = ls[last]
#     pivot_val = statistics.median([low,ls[mid],high]) 
#     # here we will get the value not index so
#     # for index a conditional statement should
#     # be brought
#     if pivot_val == low:
#         pindex= first
#     elif pivot_val == high:
#         pindex = last
#     else:
#         pindex = mid
#     # the value at pindex should be considered
#     # to swapped with first or last element
#     # for further processing
#     (ls[first],ls[pindex]) = (ls[pindex],ls[first])
#     pivot = ls[first] 
#     left = first+1
#     right = last # change right to one less than last
#     while True:
#         while left <= right and ls[left] <= pivot:
#             left +=1
#         while left <= right and ls[right] >= pivot:
#             right -=1
#         if left > right:
#             break
#         else:
#             (ls[left],ls[right]) = (ls[right],ls[left])
#     (ls[first],ls[right]) = (ls[right],ls[first])
#     return right


# def quicksort(ls,first,last):
#     if first < last:
#         p = partition(ls,first,last)
#         quicksort(ls,first,p-1)
#         quicksort(ls,p+1,last)
    

# for descending order
# just change left >= pivot and right <= pivot

def partition(ls,first,last):
    mid = (first+last)//2
    low = ls[first]
    high = ls[last]
    pivot_val = statistics.median([low,ls[mid],high]) 
    # here we will get the value not index so
    # for index a conditional statement should
    # be brought
    if pivot_val == low:
        pindex= first
    elif pivot_val == high:
        pindex = last
    else:
        pindex = mid
    # the value at pindex should be considered
    # to swapped with first or last element
    # for further processing
    (ls[first],ls[pindex]) = (ls[pindex],ls[first])
    pivot = ls[first] 
    left = first+1
    right = last # change right to one less than last
    while True:
        while left <= right and ls[left] >= pivot:
            left +=1
        while left <= right and ls[right] <= pivot:
            right -=1
        if left > right:
            break
        else:
            (ls[left],ls[right]) = (ls[right],ls[left])
    (ls[first],ls[right]) = (ls[right],ls[first])
    return right


def quicksort(ls,first,last):
    if first < last:
        p = partition(ls,first,last)
        quicksort(ls,first,p-1)
        quicksort(ls,p+1,last)


testls = [45,12,88,22,88,99,3,24]
quicksort(testls,0,len(testls)-1)
print(testls)
print(time.time()-st)
    