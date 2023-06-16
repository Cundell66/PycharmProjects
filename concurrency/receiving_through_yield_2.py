from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper(): # coroutine
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g
"""
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)
"""

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Fuck Off')
print('Hello world! Multitasking...')
greeter.send('You too')
