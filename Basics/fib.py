# implementing fibonacci series
# using recursion
import time
start_time = time.time()

# using only recursion
# def fib(n):
    
#     if  n == 0 or n == 1:
#         return(n)
#     else:
#         return fib(n-1) + fib(n-2)

# using memoization in recursion

# much more faster as we didn't have
# to revisit the fib sequence again

# def fib(n):
#     fibtable = {}
#     if n in fibtable:
#         return(fibtable[n])
#     if n == 0 or n == 1:
#         value = n
#     else:
#         value = fib(n-1) + fib(n-2)
#     fibtable[n] = value
#     return(value)

# using try catch in memoization

# def fib(n):
#     fib_table = {}
#     try:
#         if fib_table[n]:
#             return(fib_table[n])
#     except KeyError:
#         pass
#     if n == 0 or n == 1:
#         fib_table[n] = n
#         return(n)
#     else:
#         value = fib(n-1) + fib(n-2)
#     fib_table[n] = value
#     return(value)


# Using dynamic programming approach
# instead for recursive calls as well
# as memoization 
# we can generate results based on the 
# base case of memoization to obtain
# subsequent results

def fib(n):
    fibtable = {}
    fibtable[0] = 1
    fibtable[1] = 1
    for i in range(2,n+1):
        fibtable[i] = fibtable[i-1] + fibtable[i-2]
    return(fibtable[n])
    
    

print(fib(4))
print(time.time() - start_time)