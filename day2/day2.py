import re

inp = open('input.txt').readlines()

sol1 = 0
sol2 = 0
for s in inp:
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', s)
    lo = int(m.group(1))
    hi = int(m.group(2))
    lett = m.group(3)
    word = m.group(4)

    occ = 0
    for c in word:
        if c == lett:
            occ += 1
    if lo <= occ <= hi:
        sol1 += 1

    cond1 = word[lo-1] == lett
    cond2 = word[hi-1] == lett
    if cond1 ^ cond2:
        sol2 += 1

print(sol1)
print(sol2)
