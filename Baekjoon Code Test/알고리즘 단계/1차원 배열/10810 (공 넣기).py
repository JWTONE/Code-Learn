'''
5 4
1 2 3
3 4 4
1 4 1
2 2 2
'''


n, m = map(int, input().split())

b = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())

    b[i-1:j] = [0] * (j - i + 1)

    for x in range(i-1, j):
        b[x] = k

print(*b)