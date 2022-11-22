fin = open("input.txt","r")
fout = open("output.txt","a")
for l in fin.readlines():
    fout.write(l)
fin.close()
print("Values are written")
fout.close()