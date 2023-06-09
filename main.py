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

# Function to display the contents of the file with line numbers.
def display_file_contents(contents):
    for i, line in enumerate(contents):
        print(str(i) + ":" + " " + line.strip('\n'))


# Function to insert a line at a specific index.
def insert_line(content, index, line):
    content.insert(index, line)
    return content


# Function to delete a line at a specific index.
def delete_line(content, index):
    content.pop(index)
    return content


# Function to search keyword
def search_keyword(content, keyword):
    keyword_found = False
    for i, line in enumerate(content):
        if keyword in line:
            keyword_highlighted = f"\033[1;31m{keyword}\033[0m"  # You can change the color and style if needed
            line_highlighted = line.replace(keyword, keyword_highlighted)
            print(str(i) + ":" + line_highlighted.strip('\n'))
            keyword_found = True

    if not keyword_found:
        print("The word you are looking for is not in this file.")


# Function to replace specific keyword
def replace_keyword(content, keyword, replacement):
    modified_content = []
    for line in content:
        if keyword in line:
            modified_line = line.replace(keyword, replacement)
            modified_content.append(modified_line)
        else:
            modified_content.append(line)

    return modified_content


# Function to save the modified content
def save_content(file_path, content):
    write_to_file(file_path, content)
    print("Content has been saved successfully!")


# Function to display help menu
def display_help_menu():
    print("Help Menu:")
    print("-----------")
    print("open [file_path]        - Open and read the contents of a file.")
    print("write [file_path]       - Write the contents to a file.")
    print("display                 - Display the contents of the file with line numbers.")
    print("insert [index] [line]   - Insert a line at the specified index.")
    print("delete [index]          - Delete a line at the specified index.")
    print("search [keyword]        - Search for a keyword in the file.")
    print("replace [keyword] [replacement] - Replace a specific keyword with another word.")
    print("save [file_path]        - Save the modified content to a file.")
    print("help                    - Display the help menu with available commands.")
    print("exit                    - Exit the text editor.")



if __name__ == "__main__":
    print("Welcome to the command line text editor! Type 'help' to see the list of available commands.")
    file_content = []
    file_path = ""
    while True:
        user_input = input("> ")
        commands = user_input.split()
        command = commands[0]

        if command == "open":
            file_path = commands[1]
            file_content = open_and_read_file(file_path)
        elif command == "write":
            file_path = commands[1]
            write_to_file(file_path, file_content)
        elif command == "display":
            display_file_contents(file_content)
        elif command == "insert":
            index = int(commands[1])
            line = " ".join(commands[2:])
            file_content = insert_line(file_content, index, line)
        elif command == "delete":
            index = int(commands[1])
            file_content = delete_line(file_content, index)
        elif command == "search":
            keyword = commands[1]
            search_keyword(file_content, keyword)
        elif command == "replace":
            keyword = commands[1]
            replacement = commands[2]
            file_content = replace_keyword(file_content, keyword, replacement)
        elif command == "save":
            file_path = commands[1]
            save_content(file_path, file_content)
        elif command == "help":
            display_help_menu()
        elif command == "exit":
            break
        else:
            print("Invalid command. Type 'help' to see the list of available commands.")
