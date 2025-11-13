# python
import sys
from stats import number_of_words, number_of_letters, organize_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]

with open(path) as f:
    contents = f.read()

print("=============== BOOKBOT ===============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {number_of_words(contents)} total words")
print("--------- Character Count -------")
print(organize_list(contents))
print("=============== END ===============")