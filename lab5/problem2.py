import random

random_list=[random.randint(1,30) for _ in range(50)]

new_list=list(set(random_list))

print("The original list is:", random_list)
print("The list after removing duplicates is:", new_list)