num_list =[2, 1, 6]
n = 1

def solution(num_list, n):
    answer = []
    answer = num_list[:n:]
    return answer

result = solution(num_list, n)
print(result)