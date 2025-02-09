import random

random_list=[random.randint(1,10) for _ in range(20)]

print(random_list)

num=int(input("Enter the you want to find occurence:"))

position=[i for i,val in enumerate(random_list) if val==num]

print(f"{num} occured {len(position)} times")

print("The index are:",position)
