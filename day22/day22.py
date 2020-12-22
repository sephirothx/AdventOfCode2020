import copy
inp = open('input.txt').read().split('\n\n')

def score(deck):
    sol = 0
    for i, card in enumerate(reversed(deck)):
        sol += (i+1)*card
    return sol

def serialize(l):
    res = 0
    for i in l:
        res = (res << 8) + i
    return res

def play(p0, p1):
    prev0 = set()
    prev1 = set()
    while len(p0) > 0 and len(p1) > 0:
        hash0, hash1 = serialize(p0), serialize(p1)
        if hash0 in prev0 or hash1 in prev1:
            return (0, p0)
        prev0.add(hash0)
        prev1.add(hash1)

        c0, c1 = p0.pop(0), p1.pop(0)
        if c0 <= len(p0) and c1 <= len(p1):
            winner = play(copy.deepcopy(p0[:c0]), copy.deepcopy(p1[:c1]))[0]
            if winner == 0:
                p0.extend([c0,c1])
            else:
                p1.extend([c1,c0])
        else:
            if c0 > c1:
                p0.extend([c0,c1])
            else:
                p1.extend([c1,c0])
    return (0, p0) if p0 else (1, p1)

p0 = [int(x) for x in inp[0].splitlines()]
p1 = [int(x) for x in inp[1].splitlines()]
while len(p0) > 0 and len(p1) > 0:
    c0, c1 = p0.pop(0), p1.pop(0)
    if c0 > c1:
        p0.extend([c0,c1])
    else:
        p1.extend([c1,c0])
print(score(p0 if p0 else p1))

p0 = [int(x) for x in inp[0].splitlines()]
p1 = [int(x) for x in inp[1].splitlines()]
print(score(play(p0, p1)[1]))
