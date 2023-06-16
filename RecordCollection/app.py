
from utils import database


USER_CHOICE = """
Enter:
- 'a' to add a new record
- 'l' to list all records
- 'r' to mark a record played
- 'd' to delete a record
- 'q' to quit
Your choice: """


def menu():
    database.create_record_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_record()
        elif user_input == 'l':
            list_records()
        elif user_input == 'r':
            prompt_read_record()
        elif user_input == 'd':
            prompt_delete_record()

        user_input = input(USER_CHOICE)


def prompt_add_record():
    artist, title, label, album, released = input(
        'Enter the new record artist, title, label, album, released: '
    ).split(',')
    # title = input('Enter the new record title: ')

    database.add_record(artist, title, label, album, released)


def list_records():
    for record in database.get_all_records():
        #    read = 'YES' if record['read'] else 'NO'
        print(f"{record['artist']} - {record['title']} - {record['label']}, {record['album']}, {record['released']}")


def prompt_read_record():
    name = input('Enter the name of the record you\'ve played: ')

    database.mark_record_as_read(name)


def prompt_delete_record():
    name = input('Enter the name of the record you wish to delete: ')

    database.delete_record(name)


menu()
