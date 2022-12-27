import random
# Nptel Implementation

# binary heap representation using list

# max heap 
# algo
# Insert the elements while checking it with root 
# either left or right(2i+1, 2i+2)
# calculate the root as i//2-1

def max_heap(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        smallest = l
    else:
        smallest = k 
    if r < len(A) and A[r] > A[smallest]:
        smallest = r
    if smallest !=k:
        (A[k],A[smallest]) = (A[smallest],A[k])

def left(k):
    return 2*k+1

def right(k):
    return 2*k+2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n,-1,-1):
        max_heap(A,k)

example_data = []
for i in range(0,10):
    rand_num = random.randint(1,20)
    if rand_num not in example_data:
        example_data.append(rand_num)
print(example_data)
build_max_heap(example_data)
print(example_data)


# for min heap change the value to be small

def min_heap(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k 
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest !=k:
        (A[k],A[smallest]) = (A[smallest],A[k])

def left(k):
    return 2*k+1

def right(k):
    return 2*k+2

def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n,-1,-1):
        min_heap(A,k)

example_data2 = []
for i in range(0,10):
    rand_num = random.randint(1,20)
    if rand_num not in example_data2:
        example_data2.append(rand_num)

print(example_data2)
build_min_heap(example_data2)
print(example_data2)

