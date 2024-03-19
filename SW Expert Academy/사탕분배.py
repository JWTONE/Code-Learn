# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
    # A, B, K 입력
    A, B, K = map(int, input().split())

    # 작업을 반복하여 계산하지 않고 직접 계산
    diff = abs(A - B)  # 두 사람의 사탕 개수 차이 계산

    # 작업이 홀수 번 진행될 때마다 X가 2배로 늘어남
    if K % 2 == 1:
        diff *= 2

    # A, B 중 최솟값 출력
    print(min(A + diff // 2, B - diff // 2))
