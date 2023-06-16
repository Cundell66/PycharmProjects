def add_all(*args):
    return sum(args)


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')


pretty_print(**{'username': 'jose123', 'access_level': 'admin'})


print(add_all(5, 7, 3, 4))


"""
def add_all(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4

vals = {'a1': 1, 'a2': 3, 'a3': 5, 'a4': 7}

print(add_all(**vals))
"""
