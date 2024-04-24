#1
import os

def list_directories_files(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return dirs, files

def list_all_directories_files(path):
    all_dirs_files = [os.path.join(path, item) for item in os.listdir(path)]
    return all_dirs_files

path = "C:\pp2\lab6\dir"
dirs, files = list_directories_files(path)
print("Directories:", dirs)
print("Files:", files)

all_dirs_files = list_all_directories_files(path)
print("All Directories and Files:", all_dirs_files)

#2
import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

path = "C:\pp2\lab6\dir"
exists, readable, writable, executable = check_path_access(path)
print("Exists:", exists)
print("Readable:", readable)
print("Writable:", writable)
print("Executable:", executable)

#3
import os

def path_exist_get_parts(path):
    exists = os.path.exists(path)
    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return exists, filename, directory
    else:
        return exists, None, None

path = ""
exists, filename, directory = path_exist_get_parts(path)
print("Exists:", exists)
if exists:
    print("Filename:", filename)
    print("Directory:", directory)

#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = "txt"
line_count = count_lines(file_path)
print("Number of lines:", line_count)

#5
def write_list_to_file(file_path, input_list):
    with open(file_path, 'w') as file:
        for item in input_list:
            file.write(str(item) + "\n")

file_path = "txt"
input_list = [1, 2, 3, 4, 5]
write_list_to_file(file_path, input_list)

#6
import string

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    with open(file_name, 'w') as file:
        pass

#7
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src_file:
        with open(destination_file, 'w') as dest_file:
            dest_file.write(src_file.read())

source_file = ""
destination_file = ""
copy_file(source_file, destination_file)

#8
import os

def delete_file(path):
    exists = os.path.exists(path)
    if exists:
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

path_to_delete = ""
if os.path.isfile(path_to_delete):
    delete_file(path_to_delete)
else:
    print("Specified path is not a file.")
