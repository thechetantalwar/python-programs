#function with one parameter and a default value
def message(name = "Anonymous"):
    print ("hello from fucntion with one parameter and a default value ---> "+name)

user = input("Please Enter you name ")
message(user)
