import re
inp = open('input.txt').read().split('\n\n')

messages = inp[1].splitlines()
rules = {}
for l in inp[0].splitlines():
    k, r = l.split(': ')
    rules[int(k)] = r

def regex(n):
    rule = rules[n]
    if n == 8:
        return regex(42) + '+'
    if n == 11:
        x, y = regex(42), regex(31)
        m = []
        for i in range(1, 10):
            q = '{' + f'{i}' + '}'
            s = x + q + y + q
            m.append(s)
        group = '(' + '|'.join(m) + ')'
        return group
    if rule.startswith('"'):
        return rule[1]
    ret = []
    for r in rule.split(' | '):
        parts = r.split()
        s = ''
        for p in parts:
            s += regex(int(p))
        ret.append(s)
    group = '(' + '|'.join(ret) + ')'
    return group

r = regex(0)
sol = 0
for m in messages:
    sol += 1 if re.fullmatch(r, m) else 0
print(sol)
