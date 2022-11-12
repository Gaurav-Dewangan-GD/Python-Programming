# The program demonstrates that how can one use functions
# in small chunks to get the different desried results
# based on the result of previous functions

def factors(n):
    fl = []
    for i in range(1,n+1):
        if n%i == 0:
            # fl = fl +[i] 
            fl.append(i)
    return(fl)

def isprime(x):
    return(factors(x) == [1,x])

def primefactors(x):
    primelist = []
    for i in range(1,x+1):
            if isprime(i):
                primelist.append(i)
    return primelist
print(primefactors(9))

# first n prime number

def first_n_primenumbers(x):
    # count = 0
    # i = 1
    # plist = []
    
    # short syntax for multiple declaration
    (count,i,plist) = (0,1,[])
    while(count < x):
        if isprime(i):
            # count +=1
            # plist.append(i)
            (count,plist) = (count+1,plist+[i])
        i +=1
    return plist
print(first_n_primenumbers(10))
