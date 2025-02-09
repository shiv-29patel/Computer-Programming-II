import random


random_list=[random.randint(-10,10) for _ in range(30)]

positive=[num for num in random_list if num>=0]
negative=[num for num in random_list if num<0]

print("The list of positive number is:", positive)
print("The list of negative number is:", negative)