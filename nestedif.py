import sys
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

if a > b:
    if a > c:
        print ("a is largest number")
elif b > c:
    print ("b is largest number")
else:
    print ("c is largest number")
