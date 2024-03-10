n, x = map(int, input().split())
numbers = list(map(int, input().split()))

for i in numbers:
    if x > i:
        print(i, end=" ")