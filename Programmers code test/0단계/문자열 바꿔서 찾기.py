def solution(myString, pat):
    new_string = myString.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    return 1 if pat in new_string else 0

print(solution("ABBAA", "AABB"))
print(solution("ABAB", "ABAB"))