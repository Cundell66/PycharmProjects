import json

MENU_PROMPT = """\nEnter \n
                'a' to add a book, \n
                'l' to list your books, \n
                'r' to mark a book read, \n
                'd' to delete a book or \n
                'q' to quit: """


with open('books.txt', 'r') as file:
    books = json.load(file)

# books = []


def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    books.append({
        'title': title.title(),
        'author': author.title(),
        'read': False
    })
    write_file()


def list_books():
    for book in books:
        show_book(book)


def show_book(book):
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    if book['read']:
        print(f"Read It")
    else:
        print(f"Not Read")
    print(f'\n')


def read_book():
    search_title = input("Enter book title you've read: ")
    for book in books:
        if book["title"] == search_title.title():
            book["read"] = True
    write_file()


def delete_book(name):
    for book in books:
        if book['title'] == name.title():
            books.remove(book)
    write_file()


def book_delete():
    name = input("Enter title of book to delete:")
    delete_book(name)


def write_file():
    with open("books.txt", "w") as out_file:
        json.dump(books, out_file, indent=6)


user_options = {
    "a": add_book,
    "l": list_books,
    "r": read_book,
    "d": book_delete
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
