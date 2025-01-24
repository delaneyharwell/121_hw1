import re
import sys
from collections import defaultdict

def tokenize(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        tokens = re.findall(r'[a-zA-Z0-9]+', text.lower())
        return tokens
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Must provide a file")
        sys.exit(1)
    text_file_path = sys.argv[1]
    tokens = tokenize(text_file_path)