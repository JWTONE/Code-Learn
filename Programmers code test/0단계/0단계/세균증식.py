n = 2
t = 10

def solution(n, t):
    result = n
    for _ in range(1, t + 1):
        result *= 2
    return result

print(solution(2, 10))

# 세균증식 - 시간별 거듭제곱하는 수를 이용한 함수