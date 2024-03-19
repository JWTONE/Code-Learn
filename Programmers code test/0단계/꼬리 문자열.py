def solution(str_list, ex):
    answer = ""
    for string in str_list:
        if ex not in string:
            answer += string
    if answer == "":
        return answer
    else:
        return answer

print(solution(["abc", "def", "ghi"], "ef"))  # "abcghi"
print(solution(["abc", "bbc", "cbc"], "c"))   # ""
