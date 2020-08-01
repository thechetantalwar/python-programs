def readfile(filename):
    with open(filename) as f:
        line = f.readline()
        count = 1
        while line:
            print (line.strip(),"-------line ",count)
            line = f.readline()
            count = count + 1


readfile('abc.txt')

print ("Before write Operation\n")

with open('abc.txt','a') as file:
    file.write("\nAdding line svia Python\n")
    file.write("Added by Chetan\n")

readfile('abc.txt')

print ("\nAfter write Operation")
