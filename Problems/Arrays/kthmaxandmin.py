# Given an array arr[] and an integer K 
# where K is smaller than size of array, 
# the task is to find the Kth smallest or 
# largest element in the given array. 
# It is given that all array elements are 
# distinct.


def kthsmallest(arr,k):
    arr.sort()
    return(arr[k-1])
def kthhighest(arr,k):
    arr.sort()
    return(arr[-k])
print(kthhighest([7,10,4,3,20,15],3))