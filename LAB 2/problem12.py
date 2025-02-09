print("Origin of the circle: (0,0).")
r=int(input("Enter the radius of the circle:"))
x=int(input("Enter the x coordinate:"))
y=int(input("Enter the y coordinate:"))
if x*x + y*y < r*r:
    print("Point lies inside the circle.")
elif x*x + y*y > r*r:
    print("Point lies outside the circle.")
else:
    print("Point lies on the circle.")