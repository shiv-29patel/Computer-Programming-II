'''Write a program that implements a Matrix class
and performs addition, multiplication and transpose operations on 3x3 matrices.
'''

class matrix:
    def __init__(self,data):
        self.data=data
    def display(self):
        for rows in self.data:
            print(rows)
        print()
    def __add__(self,other):
        result=[]
        for i in range(3):
            row=[]
            for j in range(3):
                row.append(self.data[i][j]+other.data[i][j])
            result.append(row)
        return matrix(result)
    
    def __mul__(self,other):
        result=[]
        for i in range(3):
            row=[]
            for j in range(3):
                sum=0
                for k in range(3):
                    sum+=self.data[i][k]*other.data[k][j]
                row.append(sum)
            result.append(row)
        return matrix(result)
    def transpose(self):
        result=[]
        for i in range(3):
            row=[]
            for j in range(3):
                row.append(self.data[j][i])
            result.append(row)
        return matrix(result)                    
      



matrix1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]                
matrix2=[
    [5,3,8],
    [10,4,16],
    [9,8,19]
]

m1=matrix(matrix1)
m2=matrix(matrix2)

m1.display()
m2.display()

print("The addition matrix is")
add=(m1+m2).display()
print()

print("The multiplication matrix is:")
mul=(m1*m2).display()
print()
print("The transpose of matrix 1 is:")
t1=(m1.transpose()).display()
print()
print("The transpose of matrix 2 is:")
t2=(m2.transpose()).display()


