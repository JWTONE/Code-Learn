def solution(num_list):
    odd_sum = 0
    even_sum = 0
    
    for num1 in range(len(num_list)):
        if num1 % 2 == 0:
            even_sum += num_list[num1]
        else:
            odd_sum += num_list[num1]
            
    return max(odd_sum, even_sum)

print(solution([4, 2, 6, 1, 7, 6]))