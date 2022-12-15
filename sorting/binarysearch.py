# Python binary search program

def bs(arr,v,l,r):
    if r >=l:
        mid = (l+r) // 2
        if arr[mid] == v:
            return mid
        elif arr[mid] < v:
            return bs(arr,v,mid+1,r)
        else:
            return bs(arr,v,l,mid-1)
    else:
        return -1
searchList = list(range(1,100,1)) 
print(bs(searchList,45,0,len(searchList)-1))
    
