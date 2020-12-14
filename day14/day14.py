import re
inp = open('input.txt').read().splitlines()

mask = ''
d = {}
curr = []

def get_addr(n, mask, i=0):
    while i < len(mask):
        c = mask[i]
        if c == '1':
            n |= 1 << (35-i)
        if c == 'X':
            n |= 1 << (35-i)
            get_addr(n, mask, i+1)
            n &= ~(1 << (35-i))
            get_addr(n, mask, i+1)
            break
        i += 1
    if i == len(mask):
        curr.append(n)

for l in inp:
    a,b = l.split(' = ')
    if a == 'mask':
        mask = b
    else:
        cell = int(re.match(r'mem\[(\d+)\]', a).group(1))
        b = int(b)
        curr = []
        get_addr(cell, mask)
        for cell in curr:
            d[cell] = b

sol = 0
for v in d.values():
    sol += v
print(sol)
