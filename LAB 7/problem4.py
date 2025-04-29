str=input("Enter the string:")
dict={}
for i in str:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
            