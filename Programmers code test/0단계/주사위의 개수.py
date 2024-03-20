def solution(box, n):
    box_size = box[0] * box[1] * box[2]
    dice_count = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return dice_count

print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))