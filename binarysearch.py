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
searchList = [1,2,3,4,5,6,7,8]
print(bs(searchList,3,0,len(searchList)-1))
    
