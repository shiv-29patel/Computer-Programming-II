"""
1.Write a program to create a class that represents 
Complex numbers containing real and imaginary parts and then 
use it to perform complex number addition, subtraction,
 multiplication and division.
"""

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __str__(self):
        if self.img>=0:
         return(f"The complex number is {self.real} + i{self.img}")
        else:
           return(f"The complex number is {self.real} - i{abs(self.img)}")
    def __add__(self,other):
       real=self.real+other.real
       img=self.img+other.img
       return complex(real,img) 
    def __sub__(self,other):
        real=self.real-other.real
        img=self.img-other.img
        return complex(real,img)
    def __mul__(self,other):
       real=(self.real*other.real)-(self.img*other.img)
       img=(self.real*other.img)+(self.img*other.real)
       return complex(real,img)
    def __truediv__(self,other):
       denominator=other.real**2+other.img**2
       if denominator==0:
          raise ZeroDivisionError("cannot devide by zero")
       real=((self.real*other.real)+(self.img*other.img))/denominator   
       img=((self.img*other.real)-(self.real*other.img))/denominator
       return complex(real,img)          

c1=complex(2,5)
c2=complex(0,0)
print(c1)
print(c2)

print("The Addition is:",c1+c2)
print("The Substraction is:",c1-c2)
print("The Multiplication is:",c1*c2)
print("The Division is:",c1/c2)
