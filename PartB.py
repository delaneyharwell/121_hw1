import sys
from PartA import tokenize, compute_word_frequencies

def count_intersection(freq1, freq2):
    return len(set(freq1.keys()) & set(freq2.keys()))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Must provide 2 files to compare.")
        sys.exit(1)
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    tokens_file1 = tokenize(file1_path)
    tokens_file2 = tokenize(file2_path)
    freq1 = compute_word_frequencies(tokens_file1)
    freq2 = compute_word_frequencies(tokens_file2)
    intersection = count_intersection(freq1, freq2)
    print(intersection)