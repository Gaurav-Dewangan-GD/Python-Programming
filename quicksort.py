def quicksort(arr,l,r):
    if r - l <= 1:
        return()
    i = l+1
    for j in range(l+1,r):
        if arr[j] <= arr[l]:
            (arr[i],arr[j]) = (arr[j],arr[i])
            i +=1
    (arr[l],arr[i-1]) = (arr[i-1],arr[l])
    if(l < r):
        quicksort(arr,l,i-1)
        quicksort(arr,i,r)
