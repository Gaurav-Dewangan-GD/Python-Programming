f = open("random.txt","r")

# Reading in a file

# for each in f:
#     print(each) 

# since print statement itself
# carries a \n at end it will generate
# double spaced string
# for i in f:
#     print(i,end="")

# print(f.read()) read whole file
# print(f.read(5)) read's only 5 character
# print(f.readline()) read's one line till \n character is encountered
# print(f.readlines())
f.close()

fw = open("random.txt","a")
fw.write("\nAdded this line to random.txt")
fw.close()

