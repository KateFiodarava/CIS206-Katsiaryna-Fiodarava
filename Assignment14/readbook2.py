import xml.etree.ElementTree as ET

# Load and parse the XML data
tree = ET.parse('books.xml')
root = tree.getroot()

# Function to search for a book by title
def search_book(title):
    for book in root.findall('book'):
        book_title = book.find('title').text
        if book_title.lower() == title.lower():
            return book
    return None

# Main program loop
while True:
    user_input = input("Enter the book title (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    book = search_book(user_input)
    if book:
        author = book.find('author').text
        year = book.find('year').text
        print(f"Title: {book_title}, Author: {author}, Year: {year}")
    else:
        print(f"'{user_input}' title not found.")
