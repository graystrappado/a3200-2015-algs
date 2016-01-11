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
