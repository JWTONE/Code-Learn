n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0 
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            card_sum = cards[i] + cards[j] + cards[k] 
            if card_sum <= m:
                result = max(result, card_sum)

print(result)

# 세 카드 합 계산한뒤, M값을 넘지않는 선에서 최댓값으로 출력