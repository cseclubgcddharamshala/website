import os

EXCLUDE = {'.venv', '__pycache__'}

def print_tree(start_path, prefix=''):
    for item in sorted(os.listdir(start_path)):
        if item in EXCLUDE:
            continue
        path = os.path.join(start_path, item)
        print(prefix + '|-- ' + item)
        if os.path.isdir(path):
            print_tree(path, prefix + '|   ')

# Use current directory
print_tree('.')