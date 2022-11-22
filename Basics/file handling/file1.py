fh = open("g.txt","a")
# s = "\nThis is a string\nwritten in a file\nwithout f.close()"
# fh.write(s)
l = ["mango","orange","bear"]
fh.writelines(l)
fh.close()

# fh = open("g.txt","r")
# s = fh.read()
# print(s)
# fh.close()

