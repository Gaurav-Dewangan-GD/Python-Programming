a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# The list approach

# def gcd(m,n):
#     fm = []
#     for i in range(1,m+1):
#         if(m%i) == 0:
#             fm.append(i)
#     fn = []
#     for j in range(1,n+1):
#         if(n%j) == 0:
#             fn.append(j)
    
#     cf = []
#     for f in fm:
#         if f in fn:
#             cf.append(f)
#     return(cf[-1])

# The most recent common factor approach

# def gcd(m,n):
#         # cf = [] since list will not be efficient as value
#         # as previous value is discarded and the latest value is used
#         for i in range(1,min(m,n)+1):
#             if(m%i) == 0 and (n%i) == 0:
#                  mrcf = i # mrcf holds the most recent factor
#         return mrcf


# The scan backward approach
# instead of going 1 to min(m,n) we can go from
# largest to lowest i.e one  and return the first element
# that will be largest commond multiple or gcd


# def gcd(m,n):
#     i = min(m,n)
#     while i > 0:
#         if (m%i) == 0 and (n%i) == 0:
#             return(i)
#         else:
#             i = i-1


# Euclid's algorithm
# he suggest that if the numbers given are divisible by d
# then its difference or remainder is also divisible by d

# def gcd(m,n):
#     if n > m:
#         (m,n) = (n,m)
#     if (m%n) == 0:
#         return(n)
#     else:
#         r = m%n
#         return(gcd(n,r))

# def gcd(m,n):
#     if n > m:
#         (m,n) = (n,m)
#     if (m%n) == 0:
#         return(n)
#     else:
#         diff = m-n
#         return(gcd(max(n,diff),min(n,diff)))

# def gcd(m,n):
#     if n > m:
#         (m,n) = (n,m)
#     while (m%n) != 0:
#         (m,n) =(n,m%n)
#     return(n)

# def gcd(m,n):
#     if (m%n) == 0:
#         return n
#     else:
#         return gcd(n,m%n)

def gcd(m,n):
    if(n == 0):
        return m
    else:
        return gcd(n,m%n)

print(f"{a} and {b} gcd is {gcd(a,b)}")

