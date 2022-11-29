def minmax(arr):
    min = 0
    max = 0
    
    if len == 1:
        min = arr[0]
        max = arr[0]
        return((min,max))
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            max = arr[0]
            min = arr[1]
        else:
            max = arr[1]
            min = arr[0]
        return((min,max))
    else:
        for i in range(2,len(arr)):
            if arr[i] > max:
                max = arr[i]
            elif arr[i] < min:
                min = arr[i]
    return((min,max))
print(minmax([1,2,3,4,5]))

    