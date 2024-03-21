def solution(my_string):
    numbers = []
    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))
    return sorted(numbers)