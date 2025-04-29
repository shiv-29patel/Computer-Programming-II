name=set()

for i in range(1,6):
  a=input(f"Enter the {i} element:")
  name.add(a)

# s1=input("Enter first name:")
# name.add(s1)
# s2=input("Enter second name:")
# name.add(s2)
# s3=input("Enter third name:")
# name.add(s3)
# s4=input("Enter fourth name:")
# name.add(s4)
# s5=input("Enter fifth name:")
# name.add(s5)
print(name)

lis=list(name)
lis[4]="hello"
s=set(lis)
print(s)

el1=input("Enter the first element you want to remove:")
name.discard(el1)
el2=input("Enter the second element you want to remove:")
name.discard(el2)
print(name)


