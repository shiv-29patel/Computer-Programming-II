import csv
data=[
    ["Roll NO","Name","Subject1","Subject2","Subject3"],
    [101,"Alice",85,90,78],
    [102,"Bob",70,89,98],
    [103,"Cassy",45,50,67]
]

with open("Students.csv","w",newline='') as f:
    pen=csv.writer(f)
    pen.writerows(data)
