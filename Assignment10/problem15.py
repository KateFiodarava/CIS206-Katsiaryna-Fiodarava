#15	Write a Python program to remove multiple spaces from a string.
#Test: 
#'Python      Exercises'
import re

def remove_multiple_spaces(s):
    return re.sub(r'\s+', ' ', s).strip()

# Test case
print(remove_multiple_spaces('Python      Exercises'))  # Python Exercises
