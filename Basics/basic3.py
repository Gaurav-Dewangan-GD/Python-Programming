# Basic seraching program

# def findPos(l,v):
#     # pos = -1
#     # for i in range(len(l)):
#     #     if l[i] == v:
#     #         pos = i
#     #         break
#     # return(pos)
#     for i in range(len(l)):
#         if l[i] == v:
#             pos = i
#             break
#     else:
#         pos = -1
#     return pos
# lis = [12,33,99,65,88]
# print((findPos(lis,2)))

x = 10
del(x) # deleted value at x and assign it type undefined
try:
    x 
except NameError:
    x = 10
except:
    pass
print(x)

sample_list = list(range(0,10))
print(sample_list)
del(sample_list[4]) 
# deletes a value at sample list and 
# shifts other value to their one less 
# position
print(sample_list)

dict1 = {
    "Portugal":2,
    "Saudi":3,
    "Argentina": 4
}

print(dict1.keys())
print(dict1.values())
del(dict1["Argentina"])
print(dict1)

# Nothing or null value of empty pointers in data structure 
# or for exception handling

x = 20

if x is None:
    x = 10
else:
    x  = None
print(x)

