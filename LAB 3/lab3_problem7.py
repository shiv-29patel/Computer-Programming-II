n=int(input("Enter the value of n:"))
r=int(input("Enter the value of r:"))

n_fact=1
for i in range(1,n+1):
    n_fact*=i
r_fact=1
for i in range(1,r+1):
    r_fact*=i   
n_minus_r_fact=1
for i in range(1,n-r+1):
    n_minus_r_fact*=i 

nPr= n_fact/(n_minus_r_fact)
print("nPr=", nPr)

nCr= n_fact/r_fact*(n_minus_r_fact)
print("nCr=", nCr)

