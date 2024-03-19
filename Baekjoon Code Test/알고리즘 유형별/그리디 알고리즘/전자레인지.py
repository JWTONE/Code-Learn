import sys

T = int(sys.stdin.readline())

def Microwave(T):
    
    if T % 10 != 0:
        print(-1)
    
    else:
        a, b, c = 0, 0, 0
        a = T // 300
        b = (T % 300) // 60
        c = (T % 60) // 10
        print(a, b, c)
        
Microwave(T)
