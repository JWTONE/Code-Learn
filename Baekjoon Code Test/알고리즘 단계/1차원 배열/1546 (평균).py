n = int(input())
test = list(map(int, input().split()))

m = max(test)
sum = 0

for i in range(n):
    test[i] = test[i] / m*100
    sum += test[i]

avg = sum/n
print(avg)