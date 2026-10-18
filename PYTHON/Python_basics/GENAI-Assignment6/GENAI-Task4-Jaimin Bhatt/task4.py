'''
Task 4: File Reader with Exception Handling

Ask the user for a filename.
Try to open and read the file.
Handle:
FileNotFoundError
PermissionError
If successful, print first 3 lines of the file.
Use finally to print:

“File operation attempted.”

'''

import os

# Folder where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))

filename = input("Enter file Name : ")
filepath = os.path.join(script_dir, filename)

try:
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

except FileNotFoundError:
    print("File Not Found... Please check File Name properly.")

except PermissionError:
    print("Permission Denied you can't read this file.")

else:
    print("\nFirst three lines of the file : ")

    for line in lines[:3]:
        print(line.strip())

finally:
    print("File operation attempted")