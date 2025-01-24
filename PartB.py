import sys
from PartA import tokenize, compute_word_frequencies

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Must provide 2 files to compare.")
        sys.exit(1)
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]