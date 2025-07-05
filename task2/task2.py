def read_circle(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    cx, cy = map(float, lines[0].strip().split())
    r = float(lines[1].strip())
    f.close()
    return cx, cy, r

def read_points(file_path):
    f = open(file_path, 'r')
    points = []
    for line in f:
        x, y = map(float, line.strip().split())
        points.append((x, y))
    f.close()
    return points

def point_position(x, y, cx, cy, r):
    dx = x - cx
    dy = y - cy
    dist_squared = dx * dx + dy * dy
    r_squared = r * r
    epsilon = 1e-7
    if abs(dist_squared - r_squared) < epsilon:
        return 0
    elif dist_squared < r_squared + epsilon:
        return 1
    else:
        return 2

cx, cy, r = read_circle('circle.txt')
points = read_points('dot.txt')


for x, y in points:
    result = point_position(x, y, cx, cy, r)
    print(result)
