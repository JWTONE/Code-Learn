n = 7

def solution(slice, n):
    pizzas = 1

    while slice * pizzas < n:
        pizzas += 1

    return pizzas

print(solution(4, 12))

# 피자나눠먹기(3) - 피자를 두조각부터 열조각까지 가능한 가게에서 slice를 입력값으로 지정해주는데, 
#                 그에따라 피자수를 하나씩 + 해주며 n값에 맞춰줬다. 그러나..유사문제가 있는데