a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print("a is largest number")
elif b > c:
    print("b is largest number")
else:
    print("c is largest number")
if a < b and a < c:
    print("a is smallest number")
elif b < c:
  print("b is smallest number")
else:
    print("c is smallest number")