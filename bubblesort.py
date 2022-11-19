# Bubble sort rather than comparing to all 
# elements compares its subsequent element
# and moves the elements to their correct position

def bubblesort(arr):
    for i in range(len(arr)-1):
        swap_state = False
        for j in range(len(arr)-i-1):
            if (arr[j] >= arr[j+1]):
                (arr[j],arr[j+1]) = (arr[j+1],arr[j])
                swap_state = True
        if(swap_state == False):
            break
ls = [34,55,12,2,83,17]
print(ls)
bubblesort(ls)
print(ls)
        
             