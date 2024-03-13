mystring = "AbCdEfG"
pat = "aBc"

def solution(myString, pat):
    return int(pat.lower() in myString.lower()) 
# 문자열(a) in 문자열(b)는 문자열 a가 b에 포함되어있냐의 뜻
# True, False 로 반환되기때문에 1,0으로 출력된다.

print(solution("AbCdEfG", "aBc"))