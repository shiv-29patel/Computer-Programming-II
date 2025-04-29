def convert(string):
    s=set(string)
    st=sorted(s)
    return st

str=input("Enter a string:").split()

x=convert(str)
print(x)

