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

def compute_word_frequencies(tokens):
    freq = defaultdict(int)
    for token in tokens:
        freq[token] += 1
    return dict(freq)

def print_frequencies(freq):
    sorted_freq = sorted(freq.items(), key=lambda x: ([x[1], x[0]]))
    for token, count in sorted_freq:
        print(f"{token} -> {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Must provide a file")
        sys.exit(1)
    text_file_path = sys.argv[1]
    tokens = tokenize(text_file_path)
    frequencies = compute_word_frequencies(tokens)
    print_frequencies(frequencies)

