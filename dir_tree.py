# Task: Create a directory tree structure with color-coded output
import sys
import colorama
from pathlib import Path

if len(sys.argv) < 2:
    print("Path_to_directory is not provided.")
    sys.exit(1)


root_path = Path(sys.argv[1])
# root_path = Path(input("Enter the path to the directory: "))

i = 0
cur_dir = None
def print_dir_tree(dir_path):
    global i
    global cur_dir

    for path in dir_path.iterdir():
        if path.is_dir():
            print(colorama.Fore.BLUE + ('|' + ' '*8)*i  +  str(path.relative_to(dir_path)) + '/')
            i += 1
            cur_dir = path
            if i > 10: # Limit the depth of the directory tree to avoid too much output
                print(colorama.Fore.RED + ('|' + ' '*8)*i + '>>>')
                continue
            print_dir_tree(path)  # Recursively print subdirectories
        else: 
            if path.parent != cur_dir:
                i = i-1
            if path.name[0] == '.': # Hidden files
                print(colorama.Fore.LIGHTBLACK_EX + ('|' + ' '*8)*i + '|- ' + str(path.relative_to(dir_path)))
            else:
                print(colorama.Fore.GREEN + ('|' + ' '*8)*i + '|- ' + str(path.relative_to(dir_path)) + colorama.Fore.LIGHTBLACK_EX + ' (' + str(path.stat().st_size) + ' bytes)')
                # colorama.Style.RESET_ALL

# root_path = Path('/Users/vitaly/Documents/Work')
print_dir_tree(root_path)