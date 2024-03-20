def solution(n_str):
    # 문자열의 가장 왼쪽부터 순회하면서 첫 번째 0이 아닌 숫자가 나올 때까지 인덱스를 찾음
    idx = 0
    while idx < len(n_str) and n_str[idx] == "0":
        idx += 1
    return n_str[idx:]

print(solution("0010"))