with open("sourcefile.txt","w") as f:
    f.write("Hello i am shiv and i am learning python.")
with open("sourcefile.txt","r") as f1:
    content=f1.read()

new_content=content.upper()

with open("copy.txt","w") as f2:
    f2.write(new_content)
    