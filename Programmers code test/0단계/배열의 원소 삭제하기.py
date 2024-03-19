def solution(arr, delete_list):
    answer = []
    delete_set = set(delete_list)  

    for num in arr:
        if num not in delete_set:  
            answer.append(num)
    
    return answer

print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))  # [293, 395, 678]
print(solution([110, 66, 439, 785, 1], [377, 823, 119, 43]))  # [110, 66, 439, 785, 1]
