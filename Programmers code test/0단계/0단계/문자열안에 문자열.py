str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"
def solution(str1, str2):
    if str2 in str1:
        result = 1
    else:
        result = 2
    return result

print(solution(str1, str2))

# 문자열안에 문자열