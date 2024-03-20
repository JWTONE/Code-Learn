def sieve_of_eratosthenes(n):
    primes = [True] * (2 * n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if primes[i]:
            primes[i * i: 2 * n + 1: i] = [False] * len(primes[i * i: 2 * n + 1: i])
    
    return sum(1 for i in range(n + 1, 2 * n + 1) if primes[i])

while True:
    n = int(input())
    if n == 0:
        break
    print(sieve_of_eratosthenes(n))