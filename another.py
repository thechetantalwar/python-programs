def duplicate(list):
    newlist =[]
#    list2 = list.copy()
    i = 0
    while i < len(list):
        j = i+1
        while j < len(list):
            if list[i] == list[j]:
                list.remove(list[j])
            else:
                j = j+1
        i = i+1

    #for i in list:
    #    if  i not in newlist:
    #        newlist.append(i)
    #print(newlist)
    print (list)

list = ['UK','USA','Canada','UK','India','India','Spain','France','Spain','Germany']

duplicate(list)
