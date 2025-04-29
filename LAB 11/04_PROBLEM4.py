import os
import shutil
main=os.makedirs("main folder",exist_ok=True)

path1=os.path.join("main","sub_dir_1")

with open("path1","w") as f1:
    f1.write("Hello this is the sub directory one inside the main folder")

path2=os.path.join("main","sub_dir_2")

shutil.copyfile("path1","path2")

path=os.path.abspath(path1)

print(path)
