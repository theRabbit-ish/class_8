# using the os library change the  name of a file.

import os

# creates a file for renaming later using os library
with open("file_os.txt", "w") as f:
    f.writelines("This file is used for os library test")
    f.close()

os.rename(r"E:\python class\python_class_7\python_class_8\file_os.txt", r"E:\python class\python_class_7\python_class_8\os_file.txt")
