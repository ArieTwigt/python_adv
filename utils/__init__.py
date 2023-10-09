import os


list_files_folders = os.listdir()

folder_name = "data"

if folder_name not in list_files_folders:
    print("📂 Creating folder")
    os.mkdir(folder_name)
