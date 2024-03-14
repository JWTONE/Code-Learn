def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

print(solution([12, 4, 15, 46, 38, -2, 15]))