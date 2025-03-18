#9.	 Write a Python program to search for a literal string in a string and also find the location within the original string where the pattern occurs.
#    Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'

import re

def find_location(text, word):
    match = re.search(r'\b' + word + r'\b', text)
    if match:
        return match.start()
    return None

# Test case
print(find_location('The quick brown fox jumps over the lazy dog.', 'fox'))  # 16
