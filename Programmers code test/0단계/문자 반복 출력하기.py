my_string = 'hello'
n = 3

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer

print(solution(my_string, 3))

# 문자 반복 출력하기 - for문으로 i를 n에 곱해줬다.