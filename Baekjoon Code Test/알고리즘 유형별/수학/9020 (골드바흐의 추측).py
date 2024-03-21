def sieve_of_eratosthenes(max_num):
    prime = [True for _ in range(max_num+1)]
    p = 2
    while (p * p <= max_num):
        if (prime[p] == True):
            for i in range(p * p, max_num+1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, max_num):
        if prime[p]:
            primes.append(p)
    return primes

def find_goldbach_partition(n, primes):
    closest = min(primes, key=lambda x: abs(x - n//2))
    idx = primes.index(closest)
    
    for i in range(idx, -1, -1): 
        for j in range(idx, len(primes)):
            if primes[i] + primes[j] == n:
                return primes[i], primes[j]
            elif primes[i] + primes[j] > n:
                break  

T = int(input())

primes = sieve_of_eratosthenes(10000)
for _ in range(T):
    n = int(input())
    partition = find_goldbach_partition(n, primes)
    print(partition[0], partition[1])
