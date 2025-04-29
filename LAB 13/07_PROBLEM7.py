"""Create a class Weather that has a list containing weather parameters. 
Define an overloaded in operator that checks whether an item is present in the list. 
(Hint: define the function __contains__( )in a class.)
"""
class weather:
    def __init__(self,parameters):
        self.parameters=parameters
    def __contains__(self,item):
        return item in self.parameters   
    def __str__(self):
        return f"The weather parametres{','.join(self.parameters)}" 
    
Weather=["Sunny","Cloudy","Foggy"]

print("Rainy" in Weather)

print("Sunny" in Weather)