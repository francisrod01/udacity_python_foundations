#!/usr/bin/python3

import os
import random


def rename_files(path):
    file_list = os.listdir(path)
    print(file_list)

    for file_name in file_list:
        # Remove numbers from filename.
        # new_file_name file_name.translation(None, "0123456789")

        # Add random numbers to beginning of filename.
        new_file_name = str(random.randint(1, 99)) + file_name

        print("Renaming " + file_name + " to " + new_file_name)
        os.rename(os.path.join(path, file_name), os.path.join(path, new_file_name))


print("# Python program - Adding random numbers to beginning of filename.")

rename_files("./prank")
