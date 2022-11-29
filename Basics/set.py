# a set is a data structure
# which only contanins unique values

# declared as list with {}

colors = {'red','black','blue','red','black'}
print(colors)

# empty list

# colors = {} # wrong creates dictinary
colors2 = set()

# membership
print('black' in colors)

# passing string as set

letters = set('this is sentence')
# print(letters) # created a set with unique characters from 
# the string

# sets are like set in mathematics 
# so its operation are also same

odd = set([1,3,5,7,9,11])
prime = set([2,3,5,7,11])

# like Union
print(odd | prime) # print's union of both unique one

# intersection
print(odd & prime)

# set difference
print(odd - prime)
print(prime-odd)

# Exclusive or (union-intersection)
print(odd ^ prime)



