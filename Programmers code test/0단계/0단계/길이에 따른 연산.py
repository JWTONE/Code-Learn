import math

num_list = [2, 3, 4, 5]

def solution(num_list):
    if len(num_list) >= 11:
        result = sum(num_list)
    else:
        len(num_list) <= 10
        result = math.prod(num_list)
    return result

print(solution(num_list))

# 길이에 따른 연산
# math 라이브러리를 사용했고, num_list의 길이(len)이 11보다
# 큰지, 10보다 작은지에 대한 if문으로 더하기와, math.prod라는
# 라이브러리 곱하기를 통해 해결했다.