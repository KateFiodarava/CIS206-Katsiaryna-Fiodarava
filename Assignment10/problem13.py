#13	Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
#Test: 'Python Exercises, PHP exercises.'
import re

def replace_punctuation(s):
    return re.sub(r'[ ,.]', ':', s)

# Test case
print(replace_punctuation('Python Exercises, PHP exercises.'))  # Python:Exercises:PHP:exercises:
