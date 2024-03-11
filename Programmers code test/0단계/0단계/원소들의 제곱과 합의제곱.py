num_list = [3, 4, 5, 2, 1]

def solution(num_list):
    answer = 1
    for num in num_list:
        answer *= num

    sum_list = sum(num_list) ** 2

    if answer < sum_list:
        return 1
    else:
        return 0

print(solution(num_list))

# 원소들의 제곱과 합의제곱
# sum_list는 num_list를 제곱해주고
# 합의제곱이 기억안났는데, 원리는 파악했다.
# answer랑 sum_list를 비교해서 1, 0 출력 조건을 주었다.
# for문으로 num에 대입해주고 answer값으로 곱해주었다.