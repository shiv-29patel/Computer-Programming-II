import pandas as pd

data={
    "Name":["Rahul","Robin","Rajni"],
    "Roll No":[12,54,3],
    "Maths":[50,98,78],
    "Phy":[46,78,89],
    "Che":[67,34,38],
}

df=pd.DataFrame(data)


df.to_excel("student.xlsx",index=False)

