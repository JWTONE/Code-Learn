s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]

def solution(s1, s2):
    count = 0
    
    for s1_char in s1:
        for s2_char in s2:
            if s1_char == s2_char:
                count += 1
    
    return count

print(solution(s1, s2))

# 배열의 유사도 - s1에 있는 값을 s2에 대입하면서 맞는 개수를 result해주는 함수