#7.	Write a Python program to remove leading zeros from an IP address.
#Test: "216.08.094.196"

import re

def remove_leading_zeros(ip):
    return re.sub(r'\b0+', '', ip)

# Test case
print(remove_leading_zeros("216.08.094.196"))  # 216.8.94.196

