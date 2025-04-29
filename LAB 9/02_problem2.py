def compute(n):
    sum=n+(n+10*n)+(n+(10*n)+((10**2)*n))+(n+(10*n)+((10**2)*n)+(10**3)*n)
    
    return sum

n=int(input("Enter the number:"))

x=compute(n)
print(x)