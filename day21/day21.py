from collections import defaultdict
import re
inp = open('input.txt').read().splitlines()

d = {}
ingr = defaultdict(int)
for l in inp:
    i, a = re.match(r'(.+)\(contains (.+)\)', l).groups()
    i, a = i.split(), a.split(', ')
    for ing in i:
        ingr[ing] += 1
    for al in a:
        if al not in d:
            d[al] = set(i)
        else:
            d[al] &= set(i)

sol1 = 0
for i in d.values():
    for ing in i:
        if ing in ingr:
            del ingr[ing]
for n in ingr.values():
    sol1 += n
print(sol1)

allerg = {}
while len(allerg) < len(d):
    for a, i in d.items():
        if len(i) == 1:
            ing = i.pop()
            allerg[a] = ing
            for ii in d.values():
                if ing in ii:
                    ii.remove(ing)

allerg = sorted(allerg.items())
sol2 = ','.join(a[1] for a in allerg)
print(sol2)
