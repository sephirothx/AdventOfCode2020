from functools import reduce
inp = open('input.txt').read().split(',')
dep = 1006605

lo = dep
best = 0
for b in inp:
    if b == 'x':
        continue
    b = int(b)
    m = (dep // b + 1) * b
    if m-dep < lo:
        best = b
        lo = m-dep
print(best*lo)

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

a = []
n = []
for i, b in enumerate(inp):
    if b == 'x':
        continue
    b = int(b)
    n.append(b)
    a.append(b-i%b)
print(chinese_remainder(n, a))
