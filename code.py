def duplicate(list):
    newlist =[]
    for i in list:
        if  i not in newlist:
            newlist.append(i)
    print(newlist)

list = ['UK','USA','Canada','UK','India','India','Spain','France','Spain','Germany']

duplicate(list)
