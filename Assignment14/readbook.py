import json

# Load the JSON data
with open('books.json', 'r') as file:
    content = file.read().strip()  # .strip() to remove any extra whitespace
    if not content:
        print("The JSON file is empty!")
    else:
        data = json.loads(content)


# search for a book
def search_book(title):
    for book in data['books']:
        if book['title'].lower() == title.lower():
            return book
    return None


while True:
    user_input = input("Enter the book title (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    book = search_book(user_input)
    if book:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print(f"'{user_input}' title not found.")
