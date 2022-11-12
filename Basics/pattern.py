# for i in range(0,5):
#     for j in range(0,5):
#         print("*",end=" ")
#     print()

# i = 1 
# while(i <= 5):
#     j = 1
#     while(j <= 5):
#         print(i,end=" ")
#         j = j+1
#     print()
#     i = i+1
# itr = int(input("Enter number of iteration: "))
# for i in range(0,itr):
#     count = itr
#     for j in range(0,itr):
#         print(count,end=" ")
#         count = count -1
#     print()

# count = 1
# for i in range(0,3):
#     for j in range(0,3):
#         print(count,end=" ")
#         count = count+1
#     print()

# i = 0
# while(i < 5):
#     j = 0
#     while(j <= i):
#         print(i,end=" ")
#         j = j+1
#     print(" ")
#     i = i+1

# for i in range(1,5):
#     value = i
#     for j in range(0,i):
#         print(value,end=" ")
#         value = value+1
#     print()

# SAVING SPACE WITH LOGIC i+j-1

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i+j-1,end=" ")
#     print()

# Alphabet patterns

# alpha = 65
# for i in range(0,3):
#     for j in range(0,3):
#         print(chr(alpha),end=" ")
#     alpha = alpha+1
#     print()

# count = 0
# for i in range(5):
#     for j in range(5):
#         print(chr(65+count),end=" ")
#         count +=1
#     print()

# al  = 65
# i = 0
# while( i < 5 ):
#     j = 0
#     while( j < 5):
#         print(chr(al),end=" ")
#         j = j+1
#         al = al+1
#     i = i +1
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+i+j),end=" ")
#     print()

# count = 0
# for i in range(3):
#     for j in range(i+1):
#         print(chr(65+count),end=" ")
#         count +=1
#     print()

size = 4
for i in range(size):
    for j  in range(i+1):
        print(chr(65+size-i+j),end=" ")
    print()