def fun():
    print("You are in fun")
def disp():
    print("You are in disp")
def msg():
    print("You are in msg")

lis=[fun(),disp(),msg()]

for el in lis:
    print(el)
