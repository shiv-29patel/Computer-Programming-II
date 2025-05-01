"""7.Write a recursive function to obtain
average of all numbers present in a given list.
"""
def sum_list(lis,i=0):
    if i==len(lis):
        return 0
    else:
        return l[i]+sum_list(l,i+1)
def avg(lis):
    if len(lis)==0:
        return 0
    else:
        total=sum_list(lis)
    return total/len(lis)

l=list(map(int,input("Enter the list element separated by comma:").split(",")))
avg(l)
print("The avg of list is:",avg(l))    
