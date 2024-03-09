leaf_year = int(input())

if (leaf_year % 4 == 0 and leaf_year % 100 != 0) or (leaf_year % 400 == 0):
    print('1')
else:
    print('0')