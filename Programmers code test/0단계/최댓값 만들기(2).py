def solution(numbers):
    numbers.sort()
    max_product = numbers[-1] * numbers[-2]
    min_product = numbers[0] * numbers[1]
    return max(max_product, min_product)

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))