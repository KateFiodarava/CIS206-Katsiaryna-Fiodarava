#6.	Write a Python program that matches a word containing 'z'.
#Test: 
#"The quick brown fox jumps over the lazy dog."
#"Python Exercises."

import re

def match_z_word(s):
    pattern = "\w*z\w*"
    return bool(re.search(pattern, s))

# Test cases
print(match_z_word("The quick brown fox jumps over the lazy dog."))  # False
print(match_z_word("Python Exercises."))  # True

