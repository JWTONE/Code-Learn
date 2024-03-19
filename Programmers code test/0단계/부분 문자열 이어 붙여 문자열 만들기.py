def solution(my_strings, parts):
    answer = ""
    for i in range(len(my_strings)):
        s, e = parts[i]
        answer += my_strings[i][s:e+1]
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))  # "programmers"