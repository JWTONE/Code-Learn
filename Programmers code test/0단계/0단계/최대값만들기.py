numbers = [1, 2, 3, 4, 5]

def solution(numbers):
    st_nums = sorted(numbers, reverse=True)
    lst_nums = st_nums[:2]
    result = lst_nums[0] * lst_nums[1]
    return result

print(solution(numbers))

# 최대값만들기 - 가장 높은 수 두개를 뽑아 곱하는 방식으로 만든 함수