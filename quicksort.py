# quick sort 
# this sorting technique is also based on divide and conqueer
# but in this we didn't have to store result in other list

# First A Pivot element is selected in the list
# which can be first , last , middle or any random place in list
# then that element has to placed in right position in list
# via placing (for ascending) lower element to left and higher to right of it(pivot)
# (for descending) lower to right and higher to left
# By this we get first element sorted
# We have to do this process again and again for rest parts of list(left and right)


import time 
st = time.time()

# Partition logic to get the index where partition of list have 
# to made from where recursive process can done for remaining element

def partition(ls,first,last):
    pivot = ls[first]  # considering first element as pivot
    left = first+1     # left and right pointers
    right = last
    while True:
        while left <=right and ls[left] <= pivot:  # moving both pointer algo
            left +=1
        while left <=right and ls[right] >= pivot:
            right -=1
        if right < left: # if the condition breaks means we have break loop
                         # and process (swap) pivot and right index element
            break
        else:
          (ls[left],ls[right]) = (ls[right],ls[left]) # swapping right and left when they are in incorrect position
    (ls[first],ls[right]) = (ls[right],ls[first]) # if first element is selected then chose right else left pointer
    return right

def quicksort(ls,first,last):
    if first < last:
        p = partition(ls,first,last)    # getting index of sorted pivot element 
        quicksort(ls,first,p-1)  # repeat process for left and right parts of sorted element
        quicksort(ls,p+1,last)


testls = list(range(100,0,-1))
n = len(testls)-1
quicksort(testls,0,n)
print(testls)
print(time.time()-st)
