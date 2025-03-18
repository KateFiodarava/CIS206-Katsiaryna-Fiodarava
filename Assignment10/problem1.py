import re

def check_string(s):
    pattern = "^[a-zA-Z0-9]*$"
    return bool(re.match(pattern, s))

# Test cases
print(check_string("ABCDEFabcdef123450"))  # True
print(check_string("*&%@#!}{"))  # False
