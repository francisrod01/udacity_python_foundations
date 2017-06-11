#!/usr/bin/python3

import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir("./prank")
    print(file_list)

    # (2) for each file, rename filename
    for file_name in file_list:
        str = file_name.maketrans('', '', '0123456789')
        os.rename(file_name, file_name.translate(str))

rename_files()
