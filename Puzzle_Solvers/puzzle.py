from collections import deque
from sys import intern
import re


class Puzzle:

    pos = ""                    # default starting position

    goal = ""                   # ending position used by isgoal()

    def __init__(self, pos=None):
        if pos:
            self.pos = pos

    def __repr__(self):         # returns a string representation of the position for printing the object
        return repr(self.pos)

    def canonical(self):        # returns a string representation after adjusting for symmetry
        return repr(self)

    def isgoal(self):
        return self.pos == self.goal

    def __iter__(self):         # returns list of objects of this class
        if 0:
            yield self

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