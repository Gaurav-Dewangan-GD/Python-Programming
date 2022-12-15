
def selectionSort(arr):
   # assumption that we have consider
   # ith index element as lowest and campare it with other 
   # to find minimum

   for i in range(len(arr)):
    # creating a name to store
    # min pos
    minpos = i
    for j in range(i,len(arr)):
        if arr[j] < arr[minpos]:
            minpos = j
    # swapping with the minimum element
    (arr[i],arr[minpos]) = (arr[minpos],arr[i])

