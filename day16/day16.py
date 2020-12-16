import re
inp = open('input.txt').read().split('\n\n')

rules = [[int(x) for x in re.findall(r'\d+', l)] for l in inp[0].splitlines()]
your = [int(x) for x in inp[1].splitlines()[1].split(',')]
tickets = [[int (x) for x in l.split(',')] for l in inp[2].splitlines()[1:]]

ranges = set()
m = re.findall(r'(\d+)-(\d+)', inp[0])
for lo, hi in m:
    ranges.update(range(int(lo), int(hi)+1))

sol1 = sum(i for t in tickets for i in t if i not in ranges)
print(sol1)

def possibilities(ticket):
    ret = []
    for t in ticket:
        s = set()
        for i, r in enumerate(rules):
            l0,h0,l1,h1 = r
            if l0 <= t <= h0 or l1 <= t <= h1:
                s.add(i)
        ret.append(s)
    return ret

valid = [t for t in tickets if all(i in ranges for i in t)]
p = possibilities(your)
for ticket in valid:
    p1 = possibilities(ticket)
    for s0, s1 in zip(p, p1):
        s0 &= s1

p = {i:s for i,s in enumerate(p)}
d = {}
while p:
    for i, f in p.items():
        if len(f) == 1:
            del p[i]
            f = f.pop()
            d[f] = i
            break
    for f1 in p.values():
        f1 -= {f}

sol2 = 1
for i in (v for k,v in d.items() if k<6):
    sol2 *= your[i]
print(sol2)
