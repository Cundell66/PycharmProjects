def greet():
    friend = yield
    print(f'Hello, {friend}')


g = greet()
g.send(None)  # priming generator
g.send('Adam')