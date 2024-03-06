max_number = 0
row = 1
column = 1
# 행 = row
# 열 = column

for i in range(1, 10):
    # [1,2,3,4,5,6,7,8,9]

    # "3 23 85 34 17 74 25 52 65"
    # ["3", "23", 85 34 17 74 25 52 65"
    # [3, 23, 85, 34 ... ]
    input_list = list(map(int, input().split()))

    for j, num in enumerate(input_list, 1):
        if num > max_number:
            max_number = num
            row = i
            column = j

print(max_number)
print(row, column)
