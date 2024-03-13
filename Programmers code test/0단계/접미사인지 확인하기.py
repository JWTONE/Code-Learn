def solution(my_string, is_suffix):
    answer = my_string.endswith(is_suffix)
    return int(answer)

print(solution("banana", "ana"))
print(solution("banana", "maa"))