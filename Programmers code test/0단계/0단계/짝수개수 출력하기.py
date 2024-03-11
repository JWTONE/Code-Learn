num_list = [1, 3, 5, 7]

def solution(num_list):
    answer = [0, 0]
    
    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    
    return answer

print(solution(num_list))

# 짝수개수 출력하기 - for문으로 % 몫이 0이면 짝수를, 아니라면 홀수출력으로 해결했다