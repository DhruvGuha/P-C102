import os
import shutil



dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

from_dir = "C:/Users/Dhruv/Downloads"
to_dir = "C:/Users/Dhruv/Downloads/Downloaded_Files"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
    name , extension = os.path.splitext(file_name)
    
    if extension == "":
        continue

    for key , value in dir_tree.items():
        if extension in value:

            path1 = from_dir + '/' + file_name                       
            path2 = to_dir + '/' + key                         
            path3 = to_dir + '/' + key + '/' + file_name  

            if os.path.exists(path2):
                print("Moving " + file_name + ".....")
                # Move from path1 ---> path3
                shutil.move(path1, path3)

            else:
                os.makedirs(path2)
                print("Moving " + file_name + ".....")
                shutil.move(path1, path3)