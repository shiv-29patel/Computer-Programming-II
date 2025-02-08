string1=input("Enter the first string:")
string2=input("Enter the second string:")
found=False

# if string2 in string1:
#     print("present")
for i in range(len(string1)-len(string2)+1):
    if string1[i:i+len(string2)]==string2:
        found=True
        
        break
    
if found:
    print("String 2 is present in string 1")
else:
        print("String 2 is not present in string 1")    

