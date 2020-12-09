from itertools import combinations
inp = [int(x) for x in open('input.txt').read().splitlines()]

def is_sum(n, target):
    for i, j in combinations(inp[n-25:n], 2):
        if target == i + j:
            return True

def sum_many(target, n):
    s = 0
    i = n
    l = []
    while s < target:
        l.append(inp[i])
        s += inp[i]
        i += 1
    if s == target:
        return max(l) + min(l)

for i in range(25, len(inp)):
    if not is_sum(i, inp[i]):
        sol1 = inp[i]
        break
print(sol1)

for i in range(len(inp)):
    sol2 = sum_many(sol1, i)
    if sol2:
        break
print(sol2)
