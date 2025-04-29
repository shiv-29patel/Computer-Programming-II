lst=["madam","python","malayalam",12321]

lis1=list(filter(lambda x:str(x)==str(x)[::-1],lst))

print(lis1)