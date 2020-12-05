import re

inp = open('input.txt').read().splitlines()

def seat(bp):
    bp = re.sub(r'[FL]', '0', bp)
    bp = re.sub(r'[BR]', '1', bp)
    return int(bp,2)

z = set()
for l in inp:
    z.add(seat(l))
print(max(z))
for i in range(min(z), max(z)):
    if i not in z:
        print(i)
