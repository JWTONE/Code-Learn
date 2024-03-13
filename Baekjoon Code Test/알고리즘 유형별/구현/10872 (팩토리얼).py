import sys

N = int(sys.stdin.readline())

def Factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

print(Factorial(N))