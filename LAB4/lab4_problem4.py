str1=input("Enter the first string:")
str2=input("Enter the second string:")

for i in str2:
    str1=str1.replace(i,"")
print(str1)