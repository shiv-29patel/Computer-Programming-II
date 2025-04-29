# with open("file1.txt","w") as f1:
#     f1.write("Hello i am here\n lerning pyhton")
# with open("file2.txt","w") as f2:
#     f2.write("Hello i am here in 2\n lerning pyhton programs \n iam shiv")
def alter(file_path1,file_path2,output_path):
 with open(file_path1,"r") as file1:
     lines1=file1.readlines()

 with open(file_path2,"r") as file2:
    lines2=file2.readlines()            
   
 max_line=max(len(lines1),len(lines2))
 output_line=[]
 for i in range(max_line):
    if i<len(lines1):
        output_line.append(lines1[i])
    if i<len(lines2):
        output_line.append(lines2[i])

 with open(output_path,"w") as file:
    file.writelines(output_line)

alter("file1.txt","file2.txt","Output.txt")

