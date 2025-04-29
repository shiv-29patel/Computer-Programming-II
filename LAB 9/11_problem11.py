def intsec(list1,list2):
    intsec=[]
    for i in list1:
        if i in list2 and i not in intsec:
            intsec.append(i)
    return intsec


list1=list(map(int,input("Enter the element of list1 seperated by comma--->").split(',')))
list2=list(map(int,input("Enter the element of list2 seperated by comma--->").split(',')))

s=intsec(list1,list2)
print(s)