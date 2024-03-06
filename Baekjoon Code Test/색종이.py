def place(area, point):
    px, py = point[0], point[1]
    for x in range(10):
        for y in range(10):
            area[px+x][py+y] = 1

n = int(input())
placed_points, unplaced_points = [], []
for _ in range(n):
    point = list(map(int,input().split()))
    unplaced_points.append(point)

area = [[0 for _ in range(100)] for _ in range(100)]
while len(unplaced_points) != 0:
    point = unplaced_points.pop()
    place(area, point)

black_area = 0
for rows in area:
    for value in rows:
        black_area+=value

print(black_area)