inp = sorted(map(int, open('input.txt').readlines()))

for idx, i in enumerate(inp):
    lo = idx + 1
    hi = len(inp) - 1
    while lo < hi:
        s = i + inp[lo] + inp[hi]
        p = i * inp[lo] * inp[hi]
        if s == 2020:
            print(p)
            exit()
        if s < 2020:
            lo = lo + 1
        if s > 2020:
            hi = hi - 1
