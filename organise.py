import os, shutil

source = "C:/Users/adils/Downloads"
dest = "C:/Users/adils/Desktop"

listOfFiles = os.listdir(source);
print(listOfFiles);

for file in listOfFiles:
    root, ext = os.path.splitext(file);
    print(root,ext)
    if ext == "":
        continue;
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = source + "/" + file
        path2 = dest + "/Image Files/"
        path3 = dest + "/Image Files/" + file
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)

    if ext == ".pdf":
        path1 = source + "/" + file
        path2 = dest + "/PDF Files/"
        path3 = dest + "/PDF Files/" + file
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)

    if ext == ".exe":
        path1 = source + "/" + file
        path2 = dest + "/Executable Files/"
        path3 = dest + "/Executable Files/" + file
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)

    if ext in [".doc", ".docx"]:
        path1 = source + "/" + file
        path2 = dest + "/Document Files/"
        path3 = dest + "/Document Files/" + file
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
    