import sys
def message(name = "Anonymous"):
    print ("Hello "+name)


def fullname(fname,lname):
    print ("Fullname fucntion got called")
    print (fname+" "+lname)

#user = input("Enter your name")

message('Manikanta')

fullname(sys.argv[1],sys.argv[2])
