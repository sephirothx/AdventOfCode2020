from itertools import product
inp = open('input.txt').read().splitlines()

w = len(inp[0])
h = len(inp)

seats = {}

for i, l in enumerate(inp):
    for j, c in enumerate(l):
        seats[(i, j)] = c

def serialize(s):
    ret = ''
    for i in range(h):
        for j in range(w):
            ret += s[(i, j)]
        ret += '\n'
    return ret

def occupied(x, y):
    ret = 0
    for dx, dy in product([-1, 0, 1], repeat=2):
        if dx == dy == 0:
            continue
        dist = 1
        while (x + dx*dist, y + dy*dist) in seats and seats[(x + dx*dist, y + dy*dist)] == '.':
            dist += 1
        if (x + dx*dist, y + dy*dist) in seats and seats[(x + dx*dist, y + dy*dist)] == '#':
            ret += 1
    return ret

prev = serialize(seats)
while True:
    newseats = seats.copy()
    for i in range(h):
        for j in range(w):
            if seats[(i, j)] == 'L' and occupied(i, j) == 0:
                newseats[(i, j)] = '#'
            elif seats[(i, j)] == '#' and occupied(i, j) >= 5:
                newseats[(i, j)] = 'L'
    seats = newseats
    curr = serialize(seats)
    if curr == prev:
        break
    prev = curr

sol = sum(s == '#' for s in seats.values())
print(sol)
