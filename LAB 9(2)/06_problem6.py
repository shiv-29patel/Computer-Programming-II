"""6.A list contains some negative and 
some positive values. Write a recursive function 
that sanitizes the list by replacing all negative numbers with 0.
"""
def sanitize_lis(l,i=0):
    if i==len(l):
        return
    if l[i]<0:
        l[i]=0
    sanitize_lis(l,i+1)

l=list(map(int,input("Enter the list element separated by comma:").split(",")))
sanitize_lis(l)
print("The sanitized list is:",l)   