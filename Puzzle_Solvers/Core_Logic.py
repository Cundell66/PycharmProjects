from collections import deque
from sys import intern


def solve(pos, depthFirst=False):
    queue = deque([pos])
    trail = {intern(pos.canonical()): None}
    solution = deque()
    load = queue.append if depthFirst else queue.appendleft

    while not pos.isgoal():
        for m in pos:
            c = m.canonical()
            if c in trail:
                continue
            trail[intern(c)] = pos
            load(m)
        pos = queue.pop()

    while pos:
        solution.appendleft(pos)
        pos = trail[pos.canonical()]

    return list(solution)