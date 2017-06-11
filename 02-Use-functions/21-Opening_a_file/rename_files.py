#!/usr/bin/python3

import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir("./prank")
    saved_path = os.getcwd()
    print('Current working directory is ' + saved_path)
    os.chdir(saved_path + '/prank')

    # (2) for each file, rename filename
    for file_name in file_list:
        str = file_name.maketrans('', '', '0123456789')
        print('Old Name: ' + file_name, '- New Name: ' + file_name.translate(str))
        os.rename(file_name, file_name.translate(str))
    os.chdir(saved_path)

rename_files()
