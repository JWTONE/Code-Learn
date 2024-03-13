import sys

n = int(sys.stdin.readline())

s = "*"

for i in range(n, 0, -1):
    result = i * s
    print(result)