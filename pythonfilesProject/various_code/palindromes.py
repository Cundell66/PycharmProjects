"""
def check_if_palindrome(test_string):
    characters = list(test_string.casefold())
    characters.reverse()

    if "".join(characters) == test_string.casefold():
        print(f"{test_string} is a palindrome")
    else:
        print(f"{test_string} is not a palindrome")
"""


"""
def check_if_palindrome(test_string):
    for index, letter in enumerate(test_string.casefold(), start=1):
        if letter != test_string[-index].casefold():
            print(f"{test_string} is not a palindrome.")
            break
    else:
        print(f"{test_string} is a palindrome.")
"""


def check_if_palindrome(test_string):
    if test_string.casefold() == test_string[::-1].casefold():
        print(f"{test_string} is a palindrome.")
    else:
        print(f"{test_string} is not a palindrome.")


check_if_palindrome("Hannah")
check_if_palindrome("Peter")
