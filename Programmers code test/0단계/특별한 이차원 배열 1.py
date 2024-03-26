def solution(n):
    arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        arr[i][i] = 1 
    
    return arr

print(solution(3))  # 출력: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(solution(6))  # 출력: [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
print(solution(1))  # 출력: [[1]]
