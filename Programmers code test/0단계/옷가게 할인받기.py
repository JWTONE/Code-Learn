def solution(price):
    discount = 0
    result = 0 
    if price >= 500000:
        discount = price*0.2
        result = price
    elif price >= 300000:
        discount = price*0.1
        result = price
    elif price >= 100000:
        discount = price*0.05
        result = price
    else:
        result = price
    
    result = price - discount
    return int(result)

print(solution(580000))

# 옷가게 할인받기 - 작은수부터 배열하면 오류난다. 연산자 > 기호만 사용하면
#                 런타임 오류가 발생하므로 >= 바꿔주었다.