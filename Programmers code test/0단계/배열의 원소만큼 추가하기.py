def solution(arr):
    answer = []
    for a in arr:
        answer += [a] * a
    return answer

print(solution([5, 1, 4]))
