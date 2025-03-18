#10	Write a Python program to replace whitespaces with an underscore and vice versa.
#Test: “Regular Expressions” and “Code_Examples”

def replace_spaces(s):
    return s.replace(' ', '_').replace('_', ' ')

# Test case
print(replace_spaces("Regular Expressions"))  # Regular_Expressions
print(replace_spaces("Code_Examples"))  # Code Examples
