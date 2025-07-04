n, m = map(int, input().split())

path = []
start_ind = 0
visited_start_ind = set()

while True:
    value = start_ind + 1
    if value in visited_start_ind:
        break
    path.append(str(value))
    visited_start_ind.add(value)
    start_ind = (start_ind + m - 1) % n
    if start_ind == 0:
        break

print(''.join(path))