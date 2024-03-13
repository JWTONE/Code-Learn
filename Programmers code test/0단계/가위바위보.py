rsp = "2"

def solution(rsp):
    win_dict = {'0': '5', '2': '0', '5': '2'}
    answer = ""
    for char in rsp:
        answer += win_dict[char]

    return answer

print(solution(rsp))