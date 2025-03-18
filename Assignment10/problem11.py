#11	Write a Python program to extract year, month and date from an URL.
#Test: 
#https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/
import re

def extract_date(url):
    match = re.search(r'(\d{4})/(\d{2})/(\d{2})', url)
    if match:
        return match.groups()
    return None

# Test case
print(extract_date("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"))  # ('2016', '09', '02')
