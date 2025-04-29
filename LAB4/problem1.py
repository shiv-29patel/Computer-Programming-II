#1)Count how many vowels are there in a string. Accept the string from the user.
str=input("Enter the string:")

vovels="aeiouAEIOU"
count=0
for c in str:
    if c in vovels:
        count+=1
print(f"The number oif vovels in string is {count}")        
