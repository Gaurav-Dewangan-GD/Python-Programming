# def insertionsort(arr):
#     # it works on consideration that 
#     # the first element taken from any list
#     # is sorted one and around it the next element
#     # can be place right to it or left if the element
#     # is less than the first elements that are already sorted

#     # for i in range(len(arr)):
#     #     pos = i
#     #     while pos > 0 and arr[pos] < arr[pos-1]:
#     #         (arr[pos],arr[pos-1]) = (arr[pos-1],arr[pos])
#     #         pos -=1


# Using recursive approach

# nptel version
# def insertionsort(arr):
#     isort(arr,len(arr))

# def isort(arr,k):
#     if k > 1:
#         isort(arr,k-2)
#         insert(arr,k-2)

# def insert(arr,k):
#     pos = k
#     while pos > 1 and arr[pos] < arr[pos-1]:
#         (arr[pos],arr[pos-1]) = (arr[pos-1],arr[pos])
#         pos -=1

# assuming last one will be sorted first

def insertionsort(arr,n):
    if n <=1:
        return
    insertionsort(arr,n-1)
    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = last

    

    
