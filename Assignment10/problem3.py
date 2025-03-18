#3.	Write a Python program that matches a string that has an a followed by one or more b's.
#Test: 
#“ab”
#“abc”
#“a”
#“ab”
#“abb”

import re

def match_ab_plus(s):
    pattern = "ab+"
    return bool(re.match(pattern, s))

# Test cases
print(match_ab_plus("ab"))  # True
print(match_ab_plus("abc"))  # True
print(match_ab_plus("a"))  # False
print(match_ab_plus("ab"))  # True
print(match_ab_plus("abb"))  # True

