from utils import database

MENU_PROMPT = """ENTER:
'a' to add a book,
'l' to list your books, 
'r' to mark a book read, 
'd' to delete a book or 
'q' to quit: """


# books = []


def prompt_add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    database.add_book(title, author)


def prompt_read_book():
    search_title = input("Enter book title you've read: ")
    database.read_book(search_title)


def prompt_book_delete():
    name = input("Enter title of book to delete:")
    database.delete_book(name)


user_options = {
    "a": prompt_add_book,
    "l": database.list_books,
    "r": prompt_read_book,
    "d": prompt_book_delete
}


def menu():
    database.create_book_table()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
