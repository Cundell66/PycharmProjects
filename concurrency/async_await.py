from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():  # coroutine
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Ending...')
"""
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)
"""

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Fuck Off')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)