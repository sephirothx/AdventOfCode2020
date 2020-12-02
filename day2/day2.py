import re

inp = open('input.txt').readlines()

sol1 = 0
sol2 = 0
for s in inp:
    lo, hi, c, word = re.findall(r'(\d+)-(\d+) (\w): (\w+)', s)[0]
    lo = int(lo)
    hi = int(hi)

    if lo <= word.count(c) <= hi:
        sol1 += 1

    cond1 = word[lo-1] == c
    cond2 = word[hi-1] == c
    if cond1 ^ cond2:
        sol2 += 1

print(sol1)
print(sol2)
