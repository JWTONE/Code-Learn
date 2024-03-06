n = 15

def solution(n):
    pizzas = 1
    slices = 7
    while slices < n:
        pizzas += 1
        slices += 7
    return pizzas

print(solution(n))

# 피자나눠먹기(1) - 피자 1판에 7조각인데 모든 사람이 한조각을 먹을 수 있는 조건만들기
#                 꼬는 문제라그런지 머리아팠다.