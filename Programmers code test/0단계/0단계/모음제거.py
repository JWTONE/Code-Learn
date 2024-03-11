def solution(my_string):
    answer = ''
    mo = ["a", "e", "i", "o", "u"]
    
    for i in my_string:
        if i not in mo:
            answer += i 
    
    return answer

print(solution("bus"))

# 모음제거 - for문으로 모음을 속하지않게했다.
