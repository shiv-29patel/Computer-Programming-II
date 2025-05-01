"""Write a recursive function to obtain 
length of a given string.
"""
def str_len(s):
    if s=="":
        return 0
    else:
        return 1+str_len(s[1:])
s=input("Enter the string:")
print("The lenght of string is:",str_len(s))    