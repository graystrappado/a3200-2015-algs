from math import sqrt, floor
from itertools import chain

#faster version
def sieve_sets(n):
    if n > 3:
        yield from (2, 3)
    elif n == 3:
        yield 2
    else:
        return

    primes = set(chain(range(5, n, 6), range(7, n, 6)))
    stop, v = floor(sqrt(n)), 5
    while v <= stop:
        yield v
        primes.remove(v)
        for p in range(v * v, n, 2 * v):
            primes.discard(p)
        v = min(primes)
    yield from sorted(primes)
    
    
def sieve(n):
    primes = [m % 2 == 1 for m in range(n + 1)]
    primes[1] = False
    primes[2] = True

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for p in range(i ** 2, n + 1, 2 * i):
                primes[p] = False
    return primes

q = int(input())
print(sieve(q))
