# quick sort 
import time 
st = time.time()
def partition(ls,first,last):
    pivot = ls[first]
    left = first+1
    right = last
    while True:
        while left <=right and ls[left] <= pivot:
            left +=1
        while left <=right and ls[right] >= pivot:
            right -=1
        if right < left:
            break
        else:
          (ls[left],ls[right]) = (ls[right],ls[left])
    (ls[first],ls[right]) = (ls[right],ls[first])
    return right

def quicksort(ls,first,last):
    if first < last:
        p = partition(ls,first,last)
        quicksort(ls,first,p-1)
        quicksort(ls,p+1,last)


testls = list(range(100,0,-1))
n = len(testls)-1
quicksort(testls,0,n)
print(testls)
print(time.time()-st)
