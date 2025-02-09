x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
x3=int(input("Enter x3: "))
y3=int(input("Enter y3: "))
if (y2-y1) * (x3-x2) == (y3-y2) * (x2-x1):
    print("The points are on the same line")
else:
    print("The points are not on the same line")