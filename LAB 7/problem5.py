dict1={"banana":150,"Apple":100}
dict2={"banana":12,"Apple":10}

t=0
for i in dict1:
    for j in dict2:
        if i==j:
            t=t+(dict1[i]*dict2[j])
print(f"The total bill is {t}")            


