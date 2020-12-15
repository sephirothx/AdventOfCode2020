inp = [int(x) for x in open('input.txt').read().split(',')]

seen = {}
turn = 0
for n in inp:
    seen[n] = turn
    turn += 1

for t in range(turn, 30000000):
    t = t-1
    if inp[t] not in seen:
        inp.append(0)
    else:
        inp.append(t - seen[inp[t]])
    seen[inp[t]] = t

print(inp[-1])
