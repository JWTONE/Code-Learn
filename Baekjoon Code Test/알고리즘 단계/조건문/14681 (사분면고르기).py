x = int(input())
y = int(input())

dot = [x, y]

if dot[0] > 0 and dot[1] > 0:
    print('1')
elif dot[0] < 0 and dot[1] > 0:
    print('2')
elif dot[0] < 0 and dot[1] < 0:
    print('3')
elif dot[0] > 0 and dot[1] < 0:
    print('4')