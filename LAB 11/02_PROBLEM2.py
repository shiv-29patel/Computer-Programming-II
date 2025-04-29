import pandas as pd

df=pd.read_excel("student.xlsx")

student_dict={}

for index,row in df.iterrows():
    name=row["Name"]
    rollno=row["Roll No"]
    maths=row["Maths"]
    phy=row["Phy"]
    che=row["Che"]
    total=maths+phy+che

    student_dict[rollno]={
        "Name":name,
        "Maths":maths,
        "Phy":phy,
        "Che":che,
        "Total":total

       }
for rollno,info in student_dict.items():
    for key,value in info.items():
        print(f"{key}:{value}")
    print("-"*30)         
