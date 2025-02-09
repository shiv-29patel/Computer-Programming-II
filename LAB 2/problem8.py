angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))
if all([angle1>0,angle2>0,angle3>0]):
   if angle1 + angle2 + angle3 == 180:
      print("The triangle is valid")
   else:
     print("The triangle is not valid")
else:
   print("The triangle is not valid")