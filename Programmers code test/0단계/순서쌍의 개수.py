n = 20


def solution(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            
    return count

print(solution(20))

# 순서쌍의 개수 