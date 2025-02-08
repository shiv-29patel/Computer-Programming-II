str=input("Enter the string:")

vovels="aeiouAEIOU"
count=0
for c in str:
    if c in vovels:
        count+=1
print(f"The number oif vovels in string is {count}")        
