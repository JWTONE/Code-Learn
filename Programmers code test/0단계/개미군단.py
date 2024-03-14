def solution(hp):
    count = 0
    ant_types = [5, 3, 1]
    for ants in ant_types:
        count += hp // ants
        hp %= ants
    return count

print(solution(5))
# 그리디 알고리즘 적용함