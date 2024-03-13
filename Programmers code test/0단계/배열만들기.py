n = 10
k = 3

def solution(n, k):
    return [k * i for i in range(1, n+1) if (k * i) <= n]

print(solution(n, k))