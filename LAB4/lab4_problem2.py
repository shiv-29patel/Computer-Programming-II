"""Write you own functions(wihtout using built-in functions)to convert
    all characters of a string into lower case/upper case/toggle case
    """
string=input("Enter the string:")
lower=''
for c in string:
    x=ord(c)
    if 65<=x<=90:
        lower+=(chr(x+32))
    else: 
        lower+=(chr(ord(c)))  
print("Lower case:", lower)        

upper=''
for c in string:
    x=ord(c)
    if 97<=x<=122:
        upper+=(chr(x-32))
    else: 
        upper+=(chr(ord(c)))  
print("Upper case:", upper) 

toggle=''
for c in string:
    x=ord(c)
    if 65<=x<=90:
        toggle+=chr(x+32)
    elif 97<=x<=122: 
        toggle+=chr(ord(c)-32)  
print("toggle case:",toggle ) 
        