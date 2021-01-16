import os

# get current working directory
cur_path = os.getcwd()
print(cur_path)

# change current working directory
os.chdir('C:/Users/ASUS/Desktop')
print(os.getcwd())

# to list all files and folders
print(os.listdir())

# making new folder(directory)
os.mkdir('os test folder')
print(os.listdir())
# os.chdir('C:/Users/ASUS/Desktop/os test folder')
# print(os.getcwd())


# making nested folders(directories)
os.makedirs('folder1/ folder2/ folder3')


# view entire directory tree and files. Returns current directory names, folders in this dir, files
for dir_path, dir_names, filenames in os.walk(os.getcwd()):
    print('Current Path: ', dir_path)
    print('Directories: ', dir_names)
    print('Files: ', filenames)

# use rmdir to remove dir, use remove to remove file
os.rmdir('C:/Users/ASUS/Desktop/os test folder')
os.remove('C:/Users/ASUS/Desktop/filename')


