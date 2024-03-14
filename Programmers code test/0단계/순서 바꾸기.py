def solution(num_list, n):
    return num_list[n:] + num_list[:n]
    

print(solution([2, 1, 6], 1))