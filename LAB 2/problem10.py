length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
    print("The area of the rectangle is greater than its perimeter")
else:
    print("The perimeter of the rectangle is greater than its area")