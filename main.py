import sys
import os

# Function to open and read the contents of a file.
def open_and_read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            file_contents = file.readlines()
        return file_contents
    else:
        return []

# Function to write the contents of a file.
def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        for i, line in enumerate(content):
            file.write(line)
            if i != len(content) - 1:
                file.write('\n')