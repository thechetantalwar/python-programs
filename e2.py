
import os
contents = os.listdir('/etc')

count = len(contents)

f = open("out.txt",'w')
f.write("Total no. is "+str(count)+"\n")
f.write("Below are the contents\n")
f.close()

f = open("out.txt",'a')

for i in contents:
    i =  i.upper()
    f.write(i+"\n")

f.close()
