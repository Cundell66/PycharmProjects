movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beautiful Day In The Neighborhood", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorcese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"},
]


def find_movie(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie


find_by = input("what are we searching by? ")
looking_for = input("what are you looking for? ")
movie = find_movie(looking_for, lambda movie: movie[find_by])
print(movie or 'no movies found.')
