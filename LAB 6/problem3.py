from datetime import date

day1=int(input("Enter the day:"))
month1=int(input("Enter the month:"))
year1=int(input("Enter the year:"))

date1=(day1,month1,year1)



day2=int(input("Enter the day:"))
month2=int(input("Enter the month:"))
year2=int(input("Enter the year:"))

date2=(day2,month2,year2)

d1=date(date1[2],date1[1],date1[0])
d2=date(date2[2],date2[1],date2[0])

d=d2-d1

print("The days between two dates are:",d.days)
