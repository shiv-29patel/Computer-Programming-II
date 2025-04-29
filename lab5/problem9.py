import random

odd_lis=[random.randrange(1,100,2) for _ in range(5) ]

print(odd_lis)

even_lis=[random.randrange(2,101,2) for _ in range(4)]
print(even_lis)

odd_lis[2]= even_lis
print(odd_lis)
