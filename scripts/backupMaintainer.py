import os

path = '../backup/'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

oldest = files[0]
print(len(files))

if (len(files) > 30):
    os.remove(oldest)
else:
    print("No files were removed. Exiting.")