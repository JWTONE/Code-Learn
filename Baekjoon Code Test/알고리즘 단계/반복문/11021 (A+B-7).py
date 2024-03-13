import sys
test_case = 0
t = int(input())
for i in range(t):
        a,b = map(int, sys.stdin.readline().split())
        test_case += 1
        print(f'Case #{test_case}:',a+b)