'''4.Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape.
 The class should also have a provision to 
 accept the data relevant to the shape.
'''
import math
class shape:
    def __init__(self,type,**dimention):
        self.type=type
        self.dimention=dimention
    def perimiter(self):
        if self.type=="circle":
            r=self.dimention.get("radius")
            if r==None:
                raise ValueError("Radius required")
            return 2*math.pi*r
        elif self.type=="polygone":
            side_no=self.dimention.get("Sides")     
            side=self.dimention.get("Side_length")   
            if side==None or side_no==None:
                raise ValueError("Required attributes")
            return side*side_no
    def area(self):
        if self.type=="circle":
            r=self.dimention.get("radius")
            if r==None:
                raise ValueError("Radius required")
            return math.pi*(r**2)
        elif self.type=="polygone":
            side_no=self.dimention.get("Sides")     
            side=self.dimention.get("Side_length")   
            if side==None or side_no==None:
                raise ValueError("Required attributes")
            return (side_no*(side**2))/(4*math.tan(math.pi/side_no))

circle=shape("circle",radius=4)
print(f"The circumference of circle is {circle.perimiter()}")        
print(f"The area of circle is {circle.area()}")        
polygone=shape("polygone",Sides=6,Side_length=5)
print(f"The perimiter of polygone is {polygone.perimiter()}")        
print(f"The area of polygone is {polygone.area()}")        
        
                  