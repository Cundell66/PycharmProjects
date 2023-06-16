def prime_generator(bound):
    # your code starts here (delete the pass):
    for i in range(2, bound):
        if is_prime(i):
            yield i


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True


def prime_generator_jose(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n     # generate this prime
