T = int(input())

for test_case in range(1, T + 1):
    input_str = input().strip()

    mirror_str = ""
    for char in input_str:
        if char == 'b':
            mirror_str = 'd' + mirror_str
        elif char == 'd':
            mirror_str = 'b' + mirror_str
        elif char == 'p':
            mirror_str = 'q' + mirror_str
        elif char == 'q':
            mirror_str = 'p' + mirror_str

    print(f'#{test_case} {mirror_str}')