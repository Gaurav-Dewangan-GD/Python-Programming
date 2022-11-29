# given an array to numbers or string
# reverse it's order


# naive approach
import time
start_time = time.time()


# def reverse(arr):
#     start = 0
#     end = len(arr)-1
#     while start < end:
#         (arr[start],arr[end]) = (arr[end],arr[start])
#         start +=1
#         end -=1

# we can implement this logic using recursion 
# also via providing a base case

# def reverse(arr,start,end):
#     while start >=end:
#         return 
#     (arr[start],arr[end]) = (arr[end],arr[start])
#     reverse(arr,start+1,end-1)

# python has ways to slice an array
# we can use the negative indexing property to achieve
# reverse

def reverse(arr):
    print(arr[::-1])

list_sample = list(range(100,0,-1))
# reverse(list_sample,0,len(list_sample)-1)
# print(list_sample)
reverse(list_sample)
print("--- %s seconds ---" % (time.time() - start_time).__format__('0.5f'))

