#14	Write a Python program to find all words starting with 'a' or 'e' in a given string.
#Test: 
#"The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
import re

def find_words(s):
    return re.findall(r'\b[ae]\w*', s, re.IGNORECASE)

# Test case
test_string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(find_words(test_string))
