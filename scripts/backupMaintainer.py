#This script maintains a folder on the machine and only keeps items from the last 30 days (mins, sec, etc.)
#depending on how many backups you make and how often the script is ran.

import os

path = 'Enter backup path here..'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

oldest = files[0]
print(len(files))

if (len(files) > 30):
    os.remove(oldest)
else:
    print("No files were removed. Exiting.")
