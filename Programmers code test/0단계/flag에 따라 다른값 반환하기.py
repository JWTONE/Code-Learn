def solution(a, b, flag):
    if flag:
        result = a + b
    else:
        result = a - b
    return result

print(solution(-4, 7, True))

# flag에 따라 다른값 반환하기
# - flag값이 True면 a+b를 출력, False면 a-b로 출력