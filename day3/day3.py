inp = open('input.txt').readlines()

pos = 0
sol = 0
for s in inp:
    s = s.strip()  # apparently readlines does not strip :(
    if s[pos % len(s)] == '#':
        sol += 1
    pos += 3

print(sol)
