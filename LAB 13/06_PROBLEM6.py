"""Write a program to create a class Date that has a list containing day, 
month and year attributes. Define an overloaded == operator to compare two Date objects."""
class Date:
    def __init__(self,day,month,year):
        self.date=[day,month,year]
    def __eq__(self,other):
        return self.date==other.date
    def __str__(self):
        return f"{self.date[0]},{self.date[1]},{self.date[2]}"
    
date1=Date(29,11,2006)
date2=Date(1,5,2025)
date3=Date(29,11,2006)

print(f"{date1}=={date2}",date1==date2)
print(f"{date1}=={date3}",date1==date3)
print(f"{date2}=={date3}",date2==date3)

            
        