import random

lis=[random.randint(-15,15) for _ in range(10)]

sqr=list(map(lambda x:x**2,lis))

print("Rnadom list=",lis)
print("square list=",sqr)