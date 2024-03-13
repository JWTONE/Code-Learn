import sys

# sys.stdin = open("input.txt")

input_string = input().strip()
words = input_string.split()
string_count = 0

for i in words:
    if i.split():
        string_count += 1

print(string_count)

