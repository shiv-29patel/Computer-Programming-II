'''3.Write a program to create a class that can calculate 
the surface area and volume of a solid. 
The class should also have a provision to
 accept the data relevant to the solid.
'''
import math

class solid:
    def __init__(self,type,**dimention):
        self.type=type
        self.dimention=dimention
    def surface_area(self):
        if self.type=="cube":
            side=self.dimention.get("side")
            if side==None:
                return "Side is reqiured"
            return 6*(side**2)
        elif self.type=="sphere":
            radius=self.dimention.get("radius")
            if radius==None:
                return "Radius is required"
            return 4*math.pi*(radius**2)
        elif self.type=="cylinder":
            radius=self.dimention.get("radius")
            height=self.dimention.get("height")
            if radius==None or height==None:
                return "Radius/Height required"
            return 2*math.pi*radius*(height+radius)
    def volume(self):
        if self.type=="cube":
            side=self.dimention.get("side")
            if side==None:
                return "Side is reqiured"
            return (side**3)
        elif self.type=="sphere":
            radius=self.dimention.get("radius")
            if radius==None:
                return "Radius is required"
            return (4/3)*math.pi*(radius**3)
        elif self.type=="cylynder":
            radius=self.dimention.get("radius")
            height=self.dimention.get("height")
            if radius==None or height==None:
                return "Radius/Height required"
            return math.pi*(radius**2)*height
        
        
        
cube=solid("cube",side=3)
print(f"The surface area of cube is: {cube.surface_area()}")
print(f"The volume of cube is:{cube.volume()}")        
sphere=solid("sphere",radius=4)
print(f"The surface area of sphere is: {sphere.surface_area()}")
print(f"The volume of sphere is:{sphere.volume()}")        
cylinder=solid("cylinder",height=5,radius=8)
print(f"The surface area of cylinder is: {cylinder.surface_area()}")
print(f"The volume of cylinder is:{cylinder.volume()}")        

