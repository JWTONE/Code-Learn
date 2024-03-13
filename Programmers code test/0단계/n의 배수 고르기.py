def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer

# n의 배수 고르기 - for문으로 numlist에서 num으로 값을 옴겨주며
# if 문으로 몫을 나눈값이 0이 될때 answer에 num값을 append해준다
# 명령을 주어 해결했다.
