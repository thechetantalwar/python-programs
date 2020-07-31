import sys

a = sys.argv[1]
b = sys.argv[2]

if a > b:
    print ("a is greater")
elif a == b:
    print ("both are equal")
else:
    print ("b is greater")
