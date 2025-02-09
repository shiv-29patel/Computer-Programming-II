num = int(input("Enter a number(Only number upto six digits): "))
if num < 10:
    digits = 1
elif num < 100:
    digits = 2
elif num < 1000:
    digits = 3
elif num < 10000:
    digits = 4
elif num < 100000:
    digits = 5
else:
    digits = 6  
print(f"Number of digits: {digits}")