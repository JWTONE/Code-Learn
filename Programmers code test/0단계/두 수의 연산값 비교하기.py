a = 2
b = 91

def solution(a, b):
    result1 = int(str(a) + str(b))
    result2 = 2 * a * b
    
    if result1 > result2:
        answer = result1
    else:
        answer = result2
    
    return answer

print(solution(2, 91))

# 두 수의 연산값 비교하기

# result1은 str로 a와 b를 더한뒤에 int 사용해줬고
# result2는 곱셈값을 사용했다.

# 그 뒤 if문을 사용하여 result1과 2를 비교해주고 큰 수를 출력