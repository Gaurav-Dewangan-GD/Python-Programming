from selectionsort import *
from insertionsort import *

# recursive limit set

import sys
sys.setrecursionlimit(10000)


# list1 = [22,14,18,7,2,67]
# # list2 = list(range(1,7))
# print(list1)
# # selectionSort(list)
# insertionsort(list1,len(list1))
# print(list1)

list_long = list(range(2200,0,-1)) # works till 999 but for 1000 limit should be 
                                    # increased
insertionsort(list_long,len(list_long))
print(list_long)