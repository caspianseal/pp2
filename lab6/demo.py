import os

def delete_file(file_path):

   if os.path.exists(file_path):
       if os.access(file_path, os.W_OK):
           os.remove(file_path)
           print(f"File {file_path} deleted successfully.")
       else:
           print(f"Error: Insufficient permissions to delete file {file_path}.")
   else:
       print(f"Error: File not found at path {file_path}.")

# Example usage:
file_to_delete = "C:\pp2\lab6\dir\cbc.txt"
delete_file(file_to_delete)
