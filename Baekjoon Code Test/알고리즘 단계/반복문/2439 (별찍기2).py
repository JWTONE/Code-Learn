n = int(input())

for i in range(1, n+1):
    s = ' ' * (n - i)
    result = '*' * i
    print(s + result)