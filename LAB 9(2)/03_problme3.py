"""A string is entered through the keyboard.
 Write a recursive function that counts 
 the number of vowels in this string."""
def count_vovel(s,i=0):
    if i==len(s):
        return 0
    if s[i].lower() in "aeiou":
        return 1+count_vovel(s,i+1)
    else:
        return count_vovel(s,i+1)
    
s=input("Enter the string:")
print("The number of vovels in string is:",count_vovel(s))   
