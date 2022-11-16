def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)
    while i+j < m+n: # compares length to be in range
        if i == m: # case if first one is fully iterated
            C.append(B[j])
            j +=1   # copying the second array full
        elif j == n: # case if second one if fully iterated
            C.append(A[i])
            i +=1   # copying the first array full
        elif A[i] <= B[j]:
            C.append(A[i]) # if less append first
            i +=1
        elif A[i] > B[j]:
            C.append(B[j])
            j +=1
    return(C)



def mergesort(arr,left,right):
    if right - left <= 1:
        return(arr[left:right])
    #the divide logic
    # it will create a list
    # which will have single sorted elements
    else:
        mid = (left+right)//2 
        l = mergesort(arr,left,mid)
        r = mergesort(arr,mid,right)
        #this will merge single sorted elements
        # in a new list of sorted form
        return(merge(l,r))

