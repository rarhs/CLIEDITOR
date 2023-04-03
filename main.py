import sys
import os


def open_and_read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            file_contents = file.readlines()
        return file_contents
    else:
        return []