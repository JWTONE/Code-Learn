
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        result = 1
    else:
        result = 0
    return result

print(solution(60, 2, 3))

# 공배수
# if값으로 number % n 값과 m의 값 두개가 동일하게 0이되는 조건을
# 줬다. 