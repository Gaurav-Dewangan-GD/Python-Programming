# since merging is a common operation
# to be made throughout the list
# it can intuitive to make a common
# mergin as it has variation like
# merging for intersection elements
# union or specific condition


# merge function for intersection
# note their are a lot of built-in
# function to do so but in DSA
# we will understand the process

# assuming list givens are sorted
# def mergeIntersection(A,B):
#     (C,m,n) = ([],len(A),len(B))
#     (i,j) = (0,0)
#     while i < m and j < n:
#         if A[i] < B[j]:
#             i +=1
#         elif B[j] < A[i]:
#             j +=1
#         else:
#             C.append(B[j])
#             j +=1
#             i +=1
#     return C
# ls1 = [1,2,3,4]
# ls2 = [5,6,3,2]
# ls2.sort()
# print(mergeIntersection(ls1,ls2))


# union without duplication

def unionmerge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)
    while i < m and j < n:
        if i == m and A[i] >= B[j]:
            C.append(B[j])
            j +=1
        elif  j == n and A[i] < B[j]:
            C.append(A[i])
            i +=1
        elif(A[i] == B[j]):
            C.append(A[i])
            i +=1
    return C

ls1 = [1,2,3]
ls2 = [3,4,5]
print(unionmerge(ls1,ls2))
    
            