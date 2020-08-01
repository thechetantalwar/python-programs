import os
import sys

def list_dir(dir_name):
    return os.listdir(dir_name)

def create_file(file_name):
    f = open(file_name,'w')
    f.close()

def write_file(file_name,data):
    f = open(file_name,'a')
    f.write(data)
    f.close()

dir_name = sys.argv[1]

contents = list_dir(dir_name)
count = len(contents)
file_name = "output.txt"
create_file(file_name)
write_file(file_name,"Total no. of contents in directory "+dir_name+" is "+str(count)+"\nBelow is the list of contents \n")
for i in contents:
    i = i.upper()
    write_file(file_name,i+"\n")

