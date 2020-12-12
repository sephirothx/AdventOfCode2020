inp = open('input.txt').read().splitlines()

pos = [0, 0]
d = [10, -1]

for l in inp:
    a, n = l[0], int(l[1:])
    if a == 'N':
        d[1] -= n
    elif a == 'S':
        d[1] += n
    elif a == 'E':
        d[0] += n
    elif a == 'W':
        d[0] -= n
    elif a == 'F':
        pos[0] += d[0] * n
        pos[1] += d[1] * n
    elif a == 'R':
        for _ in range(0, n, 90):
            d[0], d[1] = -d[1], d[0]
    elif a == 'L':
        for _ in range(0, n, 90):
            d[0], d[1] = d[1], -d[0]
print(abs(pos[0]) + abs(pos[1]))
