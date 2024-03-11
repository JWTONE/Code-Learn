my_string = "abcdef"
letter = "f"


def solution(my_string, letter):
    result = ""
    for char in my_string:
        if char != letter:
            result += char
    return result

my_string = "abcdef"
letter = "f"
result = solution(my_string, letter)
print(result)

# 특정 문자열 제거하기