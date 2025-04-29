s1={"Akshay","Ahir","Botyo","Bhikho"}

a1=set()
b1=set()

for i in s1:
    if i.startswith("A"):
        a1.add(i)
    elif i.startswith("B"):
        b1.add(i)
print("The set contains name starts with A:",a1)            
print("The set contains name starts with B:",b1)            