"""A positive integer is entered through the keyboard. 
Write a function to find its binary 
equivalent of this number"""
def to_binary(n):
    if n==0:
        return ""
    else:
        return to_binary(n//2)+str(n%2)
n=int(input("Enter the number:"))

print(f"The binary conversion of {n} is:",to_binary(n))
    
