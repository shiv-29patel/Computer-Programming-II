x=int(input("Enter the number:"))
count=0

for i in range(2,x):
    if x%i==0:
        count+=1
    
if count==1:
    print(f"{x} is  prime") 

else:
    print(f"{x} is  not prime number")   

s=0
for i in range (1,x):
    if (x%i==0):
      s=s+i
if s==x:
    print(f"{x} is perfect number") 
else:
    print(f"{x} is not perfect number:")
a=x
s=str(x)
digit=sum(c.isdigit() for c in s )
sum=0
while a>0:
    sum=sum+pow(a%10,digit)
    a//=10
if x==sum:
    print(f"{x} is armstrong number:")
else:
    print(f"{x} is not armstrong number:") 

original=x
revnum=0

while x>0:
    lastdigit=x%10
    revnum=revnum*10 + lastdigit
    x//=10 
if original==revnum:
    print(f"{original} is pelindrome ")          
else:
    print(f"{original} is not pelindrome number")

sq=original**2
lastdigit=sq%10

if lastdigit==original:
    print(f"{original} is automorphic number")
else:
    print(f"{original} is not automorphic number")    