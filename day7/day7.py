import re
inp = open('input.txt').read().splitlines()

target = 'shiny gold'

regex = re.compile(r'(\d+) (.*?) bags?,?\s?')
bags = {}
for l in inp:
    bag, content = l.split(' bags contain ')
    contains = {}
    z = regex.findall(content)
    for a in z:
        contains[a[1]] = int(a[0])
    bags[bag] = contains

def containstarget(s):
    ret = target in bags[s]
    for b in bags[s]:
        ret |= containstarget(b)
    return ret

def howmany(s):
    ret = 0
    for b in bags[s]:
        ret += bags[s][b] * (1 + howmany(b))
    return ret

sol = 0
for b in bags:
    sol += containstarget(b)

print(sol)
print(howmany(target))
