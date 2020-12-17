import re
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

inp = open('input.txt').read().split('\n\n')

rules = [[int(x) for x in re.findall(r'\d+', l)] for l in inp[0].splitlines()]
your = [int(x) for x in inp[1].splitlines()[1].split(',')]
tickets = [[int (x) for x in l.split(',')] for l in inp[2].splitlines()[1:]]

ranges = set()
m = re.findall(r'(\d+)-(\d+)', inp[0])
for lo, hi in m:
    ranges.update(range(int(lo), int(hi)+1))

def possibilities(ticket):
    ret = []
    for t in ticket:
        s = [0]*len(ticket)
        for i, r in enumerate(rules):
            l0,h0,l1,h1 = r
            s[i] = l0 <= t <= h0 or l1 <= t <= h1
        ret.append(s)
    return ret

valid = [t for t in tickets if all(i in ranges for i in t)]
p = possibilities(your)
for ticket in valid:
    p1 = possibilities(ticket)
    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j] &= p1[i][j]

m = maximum_bipartite_matching(csr_matrix(p), perm_type='column')
sol = 1
for i, j in enumerate(m):
    sol *= your[i] if j < 6 else 1
print(sol)
