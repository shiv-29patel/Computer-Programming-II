import random

random_num=set()
while len(random_num)<=10:
    random_num.add(random.randint(15,45))
print(random_num)    

num_lessthan30=sum(1 for num in random_num if num<30)

print(f"There are {num_lessthan30} numbers less than 30")

random_num={num for num in random_num if num<35}


print("The set after removing element greater than 35: ",random_num)
