import heapq
import sys

lst = []
n = int(input())
for _ in range(n):
    s = int(sys.stdin.readline())
    if s != 0:
        heapq.heappush(lst,s)
    else:
        if lst:
            print(heapq.heappop(lst))
        else:
            print(0)