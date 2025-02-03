str=input("Enter the string:")
alphabets=0
digits=0

for i in str:
    x=ord(i)
    if(65<=x<=90 or 97<=x<=122):
        alphabets+=1
    elif(48<=x<=57):
        digits+=1
print("The number of alphabets are=", alphabets)                
print("The number of digits are=", digits)                