def count_lower_upper(s):
    ucount=0
    lcount=0
    for i in s:
        if i.isupper()==True:
            ucount=ucount+1
        elif i.islower()==True:
            lcount=lcount+1 
    dic={}
    dic["Upper"]=ucount         
    dic["lower"]=lcount
    return dic         

s=input("Enter the sting:")
x=count_lower_upper(s)
print(x)
