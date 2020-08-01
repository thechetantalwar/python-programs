import sys


def fullname(fname,lname):
    print ("Fullname fucntion got called")
    print (fname+" "+lname)


fullname(lname = sys.argv[1],fname = sys.argv[2])
