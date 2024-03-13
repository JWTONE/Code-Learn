str1 = "abc"	
str2 = "aabcc"

def solution(str1, str2):
    return int(str1 in str2)

print(solution("abc", "aabcc"))