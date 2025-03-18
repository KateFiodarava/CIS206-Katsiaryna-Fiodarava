#4.	Write a Python program to find sequences of lowercase letters joined by an underscore.
#Test: 
#"aab_cbbbc"
#"aab_Abbbc"
#"Aaab_abbbc"


import re

def match_lowercase_underscore(s):
    pattern = "^[a-z]+(_[a-z]+)*$"
    return bool(re.match(pattern, s))

# Test cases
print(match_lowercase_underscore("aab_cbbbc"))  # True
print(match_lowercase_underscore("aab_Abbbc"))  # False
print(match_lowercase_underscore("Aaab_abbbc"))  # False
