import sys
filename = sys.argv[1]

def readfile(filename):
    f = open(filename, 'r')
    print (f.read())

f = open(filename,'w+')
f.write("1st Line")
f.write("\n2nd Line")

f.close()


readfile(filename)


readfile('abc.txt')
