# import json
# import sqlite3

from .database_connection import DatabaseConnection

# with open('books.txt', 'r') as file:
#    books = json.load(file)


def create_book_table():

    # connection = sqlite3.connect('data.db')

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text primary key, author text, read integer)')

#    connection.commit()
#    connection.close()


def add_book(title, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES(?,?,0)', (title, author))
        except NameError:
                print(f'Book Already In Database')

#    connection.commit()
#    connection.close()


def get_all_books():
    #    connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

#    connection.close()
    return books


def list_books():
    for book in get_all_books():
        show_book(book)
    print("")


def show_book(book):
    read = "Read" if book['read'] else "Not Read"
    print(f"{book['title']} by {book['author']} is {read}.")


def read_book(search_title):
    #    connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE title=?', (search_title,))

#    connection.commit()
#    connection.close()


#    for book in get_all_books():
#        if book["title"] == search_title.title():
#            book["read"] = True
#    write_file()


def delete_book(name):
    #    connection = sqlite3.connect('data.db')
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE title=?', (name,))

#   connection.commit()
#   connection.close()


#    for book in get_all_books():
#        if book['title'] == name.title():
#            books.remove(book)
#    write_file()


# def write_file():
#    with open("books.txt", "w") as out_file:
#        json.dump(books, out_file, indent=6)
