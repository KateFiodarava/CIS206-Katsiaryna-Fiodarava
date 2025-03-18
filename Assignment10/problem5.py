#5.	Write a Python program that matches a word at the beginning of a string.
#Test:
#"The quick brown fox jumps over the lazy dog."
#" The quick brown fox jumps over the lazy dog."

import re

def match_word_at_beginning(s):
    pattern = "^\w+"
    return bool(re.match(pattern, s))

# Test cases
print(match_word_at_beginning("The quick brown fox jumps over the lazy dog."))  # True
print(match_word_at_beginning(" The quick brown fox jumps over the lazy dog."))  # False
