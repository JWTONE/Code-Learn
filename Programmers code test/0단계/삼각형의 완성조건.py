def solution(sides):
    sides.sort()
    return 1 if sides[2] < sum(sides[:2]) else 2

# 삼각형의 완성조건 (1)
# side를 정렬해주고 1번째, 2번째 인덱스의 크기와 비교해 맞지않다면
# 2를 출력하는 방식으로 적용시켰다.