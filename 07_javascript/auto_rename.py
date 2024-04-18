# 자동으로 폴더 이름의 -를 _로 바꿔주는 코드

import os

current_folder = os.getcwd()

for foldername, subfolders, filenames in os.walk(current_folder):
    if '-' in foldername:
        change_folder_name = foldername.replace('-', '_')
        os.rename(foldername, change_folder_name)
    for filename in filenames:
        if '-' in filename:
            filename = os.path.join(current_folder, change_folder_name, filename)
            change_file_name = filename.replace('-', '_')
            change_file_name = os.path.join(current_folder, change_folder_name, change_file_name)
            os.rename(filename, change_file_name)