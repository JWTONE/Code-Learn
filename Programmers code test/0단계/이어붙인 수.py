num_list = [3, 4, 5, 2, 1]

def solution(num_list):
    temp = ''
    temp1 = ''
    for i in num_list:
        if i % 2 == 0:
            temp += str(i)
        else:
            temp1 += str(i)
    return int(temp) + int(temp1)

print(solution(num_list))

# 이어붙인 수 
# 리스트에 있는 숫자를 문자열로 변환해서 짝수,홀수로 나누어준다.
# 짝수끼리 더해준 값과 홀수끼리 더해준 값을 합치면 끝