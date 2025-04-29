import json

class Employee:
    def __init__(self, code, name, date, salary):
        self.code = code
        self.name = name
        self.date = date
        self.salary = salary


obj = Employee(101, "Robin", "2023-03-29", 12000)


with open("employee.txt", "w") as f1:
    json.dump(obj.__dict__, f1)


with open("employee.txt", "r") as f2:
    data = json.load(f2)


new_obj = Employee(**data)

print("Employee Code:", new_obj.code)
print("Name:", new_obj.name)
print("Date of Joining:", new_obj.date)
print("Salary:", new_obj.salary)
