cards = [input().split() for _ in range(5)]
colors = [card[0] for card in cards]
numbers = sorted([int(card[1]) for card in cards])

color_count = {color: colors.count(color) for color in set(colors)}
number_count = {number: numbers.count(number) for number in set(numbers)}

# 규칙 1: 같은 색, 연속 숫자
is_same_color = len(set(colors)) == 1
is_consecutive = all(numbers[i] - numbers[i-1] == 1 for i in range(1, 5))

# 규칙 2: 4장 숫자 같음
four_of_a_kind = 4 in number_count.values()

# 규칙 3: 풀 하우스 (3장 같고, 2장 같음)
full_house = sorted(number_count.values()) == [2, 3]

# 규칙 4: 플러시 (모든 카드 같은 색)
flush = is_same_color

# 규칙 5: 스트레이트 (모든 카드 연속 숫자)
straight = is_consecutive

# 규칙 6: 쓰리 오브 어 카인드
three_of_a_kind = 3 in number_count.values()

# 규칙 7: 투 페어
two_pair = sorted(number_count.values()).count(2) == 2

# 규칙 8: 원 페어
one_pair = sorted(number_count.values()).count(2) == 1

# 점수 계산
if is_same_color and is_consecutive:
    score = 900 + numbers[-1]
elif four_of_a_kind:
    score = 800 + [number for number, count in number_count.items() if count == 4][0]
elif full_house:
    score = 700 + [number for number, count in number_count.items() if count == 3][0]*10 + [number for number, count in number_count.items() if count == 2][0]
elif flush:
    score = 600 + numbers[-1]
elif straight:
    score = 500 + numbers[-1]
elif three_of_a_kind:
    score = 400 + [number for number, count in number_count.items() if count == 3][0]
elif two_pair:
    pairs = sorted([number for number, count in number_count.items() if count == 2], reverse=True)
    score = 300 + pairs[0]*10 + pairs[1]
elif one_pair:
    score = 200 + [number for number, count in number_count.items() if count == 2][0]
else:
    score = 100 + numbers[-1]

print(score)
