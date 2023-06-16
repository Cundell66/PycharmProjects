records_file = 'utils/recordcollection.txt'


def create_record_table():
    with open(records_file, 'r') as file:
        pass  # just to make sure the file is there


def get_all_records():
    with open(records_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'artist': line[0], 'title': line[1], 'label': line[2], 'album': line[3], 'released': line[4]}
        for line in lines
    ]


def add_record(artist, title, label, album, released):
    with open(records_file, 'a') as file:
        file.write(f'{artist},{title},{label},{album},{released} 0\n')


def _save_all_records(records):
    with open(records_file, 'w') as file:
        for record in records:
            file.write(
                f"{record['artist']},{record['title']},{record['label']},{record['album']},{record['released']}\n"
            )


def mark_record_as_read(title):
    records = get_all_records()
    for record in records:
        if record['title'] == title:
            record['read'] = 1
    _save_all_records(records)


def delete_record(title):
    records = get_all_records()
    records = [record for record in records if record['title'] != title]
    _save_all_records(records)


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
