def solution(my_string):
    ns = []
    for i in my_string:
        if i.isdigit():
            ns.append(int(i))
    answer = sum(ns)
    return answer

print(solution("asbdfsa123"))

# 숨어있는 숫자의 덧셈 - 문자열은 빼주고 숫자만 다시 ns 리스트에
# 추가해주는식으로 만들어보았다