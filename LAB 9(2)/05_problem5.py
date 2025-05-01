"""Calculate ab where a and b received 
through the keyword using recursion.
"""
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

a=int(input("Enter the number:"))
b=int(input("Enter the power:"))
print(f"{a}^{b} is=",power(a,b))  
    