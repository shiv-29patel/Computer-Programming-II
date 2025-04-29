
def sum_avg():
    a=int(input("Enter the marks for sub1:"))
    b=int(input("Enter the marks for sub2:"))
    c=int(input("Enter the marks for sub3:"))
    d=int(input("Enter the marks for sub4:"))
    e=int(input("Enter the marks for sub5:"))

    total=a+b+c+d+e
    avg=total/5
    dict1 = {'Total':total, 'Average':avg}
    return dict1

def unpack(*dictionary):
    print("Total: {Total}, Average: {Average}")


x=sum_avg()
print(x)
unpack(**x)