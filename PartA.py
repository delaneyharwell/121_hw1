import re
import sys
from collections import defaultdict

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Must provide a file")
        sys.exit(1)
    text_file_path = sys.argv[1]