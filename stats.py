# python

# stats.py contains the function that counts the number of words in a text

from collections import Counter
import string

def number_of_words(file_contents):
    words = file_contents.split()
    return len(words)

def number_of_letters(file_contents):
    text = file_contents.lower()
    return Counter(text)

def organize_list(text):
    letter_list = Counter(text.lower())
    for ch, n in letter_list.most_common():
        if ch.isalpha():
            print(f"{ch}: {n}")