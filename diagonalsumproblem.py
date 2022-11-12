def diagonalDifference(arr):
    # Write your code here
    sumr = 0
    suml = 0
    l = len(arr)
    for i in range(l):
        for j in range(l):
            if i == j:
                sumr += arr[i][j]
                print(sumr)
            if (i+j== l-1 ):
                suml += arr[i][j]
                print(suml)
    return(abs(suml-sumr))

arr2 = [[11,2,4],[4,5,6],[10,8,-12]]
# print(len(arr2))
result  = diagonalDifference(arr2)
print(result)
# print(result)