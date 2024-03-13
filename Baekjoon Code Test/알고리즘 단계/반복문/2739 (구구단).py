n = int(input())

def table(n):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for j in num:
        result = n * j
        print(f"{n} * {j} = {result}")

table(n)

# 구구단 list값을 j로 넣고 f string으로 출력해서 baekjoon 사이트에 맞게 했다.