list1=[1,2,3,5,6,78,42,50]

list2=[1,2,3,56,7,8,61]

list3=[]

for num in  list1:
    if num not in list2:
        list3.append(num)
       
print(list3)            