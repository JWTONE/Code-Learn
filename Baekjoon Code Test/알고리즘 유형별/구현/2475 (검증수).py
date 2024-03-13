N = map(int, input().split())

add = 1
total = 0

for i in N:
    add = i*i
    total += add

result = total % 10

print(result)
