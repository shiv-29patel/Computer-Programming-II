tup=(1,2,3,4,5,6,"hello")

print(tup)

lis=list(tup)

a="hello"

for el in lis:
    if el==a:
        lis.remove(el)
print("New tuple is",tuple(lis))        