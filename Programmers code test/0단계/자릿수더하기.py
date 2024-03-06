n = 1234
n2 = 930211

def solution(n):
    answer = sum(int(digit) for digit in str(n))
    return answer

print(solution(n))

# 자릿수더하기