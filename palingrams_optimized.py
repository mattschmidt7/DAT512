#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:19:49 2024

@author: mschmidt
"""

import load_dictionary

import time
start_time = time.time()

# Load the word list from the dictionary file
word_list = load_dictionary.load("/Users/mschmidt/Desktop/Spring 2024/DAT 512/dictionary.txt")

def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)

    # Iterate through each word in the word_list
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]

        # Check for palingrams with the remaining part of the reversed word
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))

    return pali_list

# Find palingrams
palingrams = find_palingrams()

# Sort palingrams on the first word
palingrams_sorted = sorted(palingrams)

# Display the list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))

end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))
    