area = [[0]*100 for _ in range(100)]
# 100x100사이즈 영역

n = int(input())
# 색종이 수 입력받음

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            area[i][j]= 1
# 색종이 붙이기

black_area = sum(row.count(1) for row in area)
# 중첩영역 = 1 계산

print (black_area)