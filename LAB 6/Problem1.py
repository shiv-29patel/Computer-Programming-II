lis=[("PRIYANK", "KRISHNA"),("MIHIR","AYUSH"),"RUTU","AKANKSHA","TANVI"]
bcount=0
gcount=0
for i in lis:
    # if type(i)==tuple:
    #     for j in i:
    if isinstance(i,tuple):
            bcount+=len(i)
    else:
        gcount+=1 
print("The number of boys=", bcount)
print("The number of girls=", gcount)
