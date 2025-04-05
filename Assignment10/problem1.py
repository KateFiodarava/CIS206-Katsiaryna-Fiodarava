#1.	Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

#Test: 
#"ABCDEFabcdef123450"
#"*&%@#!}{"


import re

def check_string(s):
    pattern = "^[a-zA-Z0-9]*$"
    return bool(re.match(pattern, s))

# Test cases
print(check_string("ABCDEFabcdef123450"))  # True
print(check_string("*&%@#!}{"))  # False
