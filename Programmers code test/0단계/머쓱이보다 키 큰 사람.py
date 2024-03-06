array = [149, 180, 192, 170]
height = 167

def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

print(solution(array, height))

# 머쓱이보다 키 큰 사람