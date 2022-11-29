# given an array
# of 0's,1's and 2's only

# we have sort them in ascending order
import time
start_time = time.time()


def sort1(arr):

    # implemented using insertion sort
    # for i in range(len(arr)):
    #     pos = i
    #     while pos > 0 and arr[pos] < arr[pos-1]:
    #         (arr[pos],arr[pos-1]) = (arr[pos-1],arr[pos])
    #         pos -=1
    
    # approach 
    # we can divide the array in three half like 
    # 0 to low,low to mid,mid to high
    #  0 , 1,2
    
    # if we get the elements in high area that are to be 
    # at lower position we just swap them and increment 
    # and decrement their values
    lo = 0
    high = len(arr) - 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            (arr[lo], arr[mid]) = (arr[mid], arr[lo])
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            (arr[mid], arr[high]) = (arr[high],arr[mid])
            high -= 1
list_sample = [0,2,1,0,2,2]
print(list_sample)
print(f"time taken: {time.time()-start_time}")