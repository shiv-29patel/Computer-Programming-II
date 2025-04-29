def lis_tup(n):
    lis=[(x,x**2,x**3) for x in range(1,n+1)]
    return lis

x=int(input("Enter the end value:"))

list1=lis_tup(x)
print(list1)