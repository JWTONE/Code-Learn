def solution(my_string, target):
    return int(target.lower() in my_string.lower())

print(solution("banana", "ana"))