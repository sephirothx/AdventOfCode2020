from itertools import product
inp = open('input.txt').read().splitlines()

def solve(dim, cycles=6):
    def neighbors(c, count_self=True):
        for delta in product([-1,0,1], repeat=dim):
            if not count_self and all(d==0 for d in delta):
                continue
            yield tuple(x+d for x,d in zip(c,delta))
    d = set()
    for y, l in enumerate(inp):
        for x, c in enumerate(l):
            if c == '#':
                d.add(tuple([x,y] + [0]*(dim-2)))
    for _ in range(cycles):
        s = set(n for c in d for n in neighbors(c))
        new_d = set()
        for c in s:
            active = 0
            for n in neighbors(c,False):
                active += 1 if n in d else 0
            if c in d and 2<=active<=3:
                new_d.add(c)
            elif c not in d and active == 3:
                new_d.add(c)
        d = new_d
    return len(d)

print(solve(3))
print(solve(4))
