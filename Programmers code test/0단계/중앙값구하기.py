array = [7, 8, 15, 11, 1]

def solution(array):
    sort_array = sorted(array)
    md_list = len(sort_array) // 2
    md_value = sort_array[md_list]
    return md_value

result = solution(array)

print(array, result)

# # 중앙값구하기