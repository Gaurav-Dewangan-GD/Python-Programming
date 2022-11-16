from selectionsort import *
from insertionsort import *
from mergesort import*
# recursive limit set

import sys
sys.setrecursionlimit(10000)


# list1 = [22,14,18,7,2,67]
# # list2 = list(range(1,7))
# print(list1)
# # selectionSort(list)
# insertionsort(list1,len(list1))
# print(list1)

# list_long = list(range(2200,0,-1)) # works till 999 but for 1000 limit should be 
#                                     # increased
# insertionsort(list_long,len(list_long))

list_long = list(range(1,100,2)) + list(range(0,100,2))
# list_long = [34,25,81,99,12,1]

# ls1 = [1,2,3]
# ls2 = [12,8,7]
# print(merge(ls1,ls2))
# print(list_long)
new_sorted_list = mergesort(list_long,0,len(list_long))
print(new_sorted_list)