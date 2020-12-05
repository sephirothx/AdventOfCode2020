inp = open('input.txt').read().splitlines()

def seat(bp):
    rl, rh = 0, 127
    cl, ch = 0, 7
    for c in bp:
        if c=='F':
            rh=(rh+rl)//2
        if c=='B':
            rl=(rh+rl+1)//2
        if c=='R':
            cl=(ch+cl+1)//2
        if c=='L':
            ch=(ch+cl)//2
    return rl*8+cl

z = set()
for l in inp:
    z.add(seat(l))
print(max(z))
for i in range(min(z), max(z)):
    if i not in z:
        print(i)
