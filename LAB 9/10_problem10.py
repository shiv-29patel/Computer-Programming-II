def frequency(string):
    dict={}
    s=string.split()
    for i in s:
        i=i.lower()
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return sorted(dict.items())

x=input("Enter a string:")

d=frequency(x)

print(d)