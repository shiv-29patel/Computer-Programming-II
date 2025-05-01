"""4.Write a recursive function that reverses 
the list of numbers that it receives."""

def lis_rev(lis):
    if len(lis)<=1:
        return lis
    else:
        return lis_rev(lis[1:])+[lis[0]]

l=list(map(int,input("Enter the list element sapereted by coma").split(",")))

print("The revesed list is:",lis_rev(l))


