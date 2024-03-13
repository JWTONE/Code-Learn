from collections import deque

def card_2(n):
    card = deque(range(1, n+1))
    
    while len(card) > 1:        
        pop_card = card.popleft()
        move_card = card.popleft()
        card.append(move_card)
    
    return card[0]

n = int(input())
result = card_2(n)
print(result)