n = 10
k = 3

def solution(n, k):
    yang_price = 12000
    drink = 2000

    order_yang_price = n * yang_price
    order_drink_price = k * drink
    discount = min(n // 10 , k) * drink

    total = order_drink_price + order_yang_price - discount

    return total

print(solution(10, 3))

# 양꼬치 - 수학적 개념을 어떻게 적용시켜야할지 공식같은게 떠오르지않아서
#         그대로 대입해가며 해결했다.