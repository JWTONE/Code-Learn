T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))

    total = sum(num_list)
    avg = total / len(num_list)
    result = round(avg)  # 평균을 반올림한 정수로 변환

    print(f'#{test_case} {result}')
    
## 아래는 간략화

T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    result = round(sum(num_list) / len(num_list))

    print(f'#{test_case} {result}')