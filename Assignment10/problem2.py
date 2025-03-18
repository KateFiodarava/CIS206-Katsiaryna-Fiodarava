#2.	Write a Python program that matches a string that has an a followed by zero or more b's.
#Test: 
#“ab”
#“abc”
#“a”
#“ab”
#“abb”


import re

def match_ab(s):
    pattern = "ab*"
    return bool(re.match(pattern, s))

# Test cases
print(match_ab("ab"))  # True
print(match_ab("abc"))  # True
print(match_ab("a"))  # True
print(match_ab("ab"))  # True
print(match_ab("abb"))  # True

