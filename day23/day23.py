inp = [int(c) for c in "792845136"]
MAX = max(inp)

curr = 0
for _ in range(100):
    inp = inp[curr:] + inp[:curr]
    r = inp[1:4]
    inp = inp[:1] + inp[4:]
    dest = inp[0]
    while True:
        dest = dest-1 if dest>1 else MAX
        if dest not in r:
            break
    i = inp.index(dest)
    inp = inp[:(i+1)] + r + inp[(i+1):]
    inp = inp[-curr:] + inp[:-curr]
    curr = (curr + 1) % len(inp)
idx = inp.index(1)
print(''.join(str(i) for i in inp[idx+1:] + inp[:idx]))

inp = [int(c) for c in "792845136"] + list(range(10, 10**6 + 1))
MAX = max(inp)

class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None

d = {i: Cup(i) for i in inp}
for i in range(len(inp)):
    d[inp[i]].next = d[inp[(i+1)%MAX]]

curr = d[inp[0]]
for it in range(10**7):
    c1,c2,c3 = curr.next, curr.next.next, curr.next.next.next
    dest = curr.value
    while True:
        dest = dest-1 if dest>1 else MAX
        if dest not in (c1.value, c2.value, c3.value):
            break
    dest = d[dest]
    curr.next = c3.next
    c3.next = dest.next
    dest.next = c1
    curr = curr.next

a = d[1].next.value
b = d[a].next.value
print(a*b)
