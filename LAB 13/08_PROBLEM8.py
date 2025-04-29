"""8.Implement a String class containing the following functions:
a.Overloaded += operator function to perform string concatenation
b.Method toLower() to convert upper case letters to lower case.
c.Method toUpper() to convert lower case letters to upper case.
"""
class string:
    def __init__(self,value):
        self.value=value
    def __iadd__(self,other):
        if isinstance(other,string):
            self.value+=other.value
        elif isinstance(other,str):
            self.value+=other    
        else:
            raise TypeError("Only strin/str can be added")
        return self
    
    def toLower(self):
        self.value = self.value.lower()
    
    def toUpperr(self):
        self.value=self.value.upper()
    
    def __str__(self):
        return self.value
 
s1=string("Learning")
s2=string("Python")
s1+=s2
print(s1)
s1.toLower()
print("After converting to lower case: ",s1)
s1.toUpperr()
print("After converting to upper case: ",s1)


               