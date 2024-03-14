import sys

money = int(sys.stdin.readline())
changes = 1000 - money

count = 0
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += changes // coin
    changes %= coin

print(count)