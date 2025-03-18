#8.	Write a Python program to search for literal strings within a string.
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'


import re

def search_words(text, words):
    return [word for word in words if re.search(r'\b' + word + r'\b', text)]

# Test case
print(search_words('The quick brown fox jumps over the lazy dog.', ['fox', 'dog', 'horse']))  # ['fox', 'dog']

