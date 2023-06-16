import generate_target

MENU_PROMPT = "\nEnter 'y' to play again, or 'q' to quit: "

"""
user_options = {
    "a": generate_target,
    # "l": list_movie,
    # "f": find_movie
}
"""


def menu():
    selection = input(MENU_PROMPT)
    while selection.lower() != 'q':
        if selection.lower() == 'y':
            n = generate_target.generate_numbers()
            generate_target.run(n)
            # selected_function = user_options[selection]
            # selected_function
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
