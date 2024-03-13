arr = [1, 2, 3, 100, 99, 98]
k = 3

def solution(arr, k):
    answer = []
    if k % 2 == 1:
        answer = [num_list * k for num_list in arr]
    else:
        answer = [num_list + k for num_list in arr]
    return answer

answer = solution(arr, k)
print(answer)