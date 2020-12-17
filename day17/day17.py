from itertools import product
inp = open('input.txt').read().splitlines()

def neighbors(x,y,z,w, count_self=True):
    for dx,dy,dz,dw in product([-1,0,1], repeat=4):
        if not count_self and dx == dy == dz == dw == 0:
            continue
        yield (x+dx, y+dy, z+dz, w+dw)

d = set()
for y, l in enumerate(inp):
    for x, c in enumerate(l):
        if c == '#':
            d.add((x,y,0,0))

for _ in range(6):
    s = set([c for x,y,z,w in d for c in neighbors(x,y,z,w)])
    new_d = set()
    for x,y,z,w in s:
        active = 0
        for n in neighbors(x,y,z,w,False):
            active += 1 if n in d else 0
        if (x,y,z,w) in d and 2<=active<=3:
            new_d.add((x,y,z,w))
        elif (x,y,z,w) not in d and active == 3:
            new_d.add((x,y,z,w))
    d = new_d

sol = len(d)
print(sol)
