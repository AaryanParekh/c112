import os
import shutil
source="C:/Users/aarya/Downloads"
destination="C:/Users/aarya/Desktop"
list_of_files=os.listdir(source)
print(list_of_files)

for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    if extention=='':
        continue
    if extention in ['.gif','.png','.jpg','.jpeg','.jfif','.pdf']:
        path1=source+'/'+file_name
        path2=destination+'/'+'Image_Files'
        path3=destination+'/'+'Image_Files'+'/'+file_name

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)