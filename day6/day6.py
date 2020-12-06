inp = open('input.txt').read().split('\n\n')

def count1(s):
    s = s.replace('\n','')
    ans = set(s)
    return len(ans)

def count2(s):
    s = s.splitlines()
    ans = set(s[0])
    for l in s[1:]:
        ans1 = set(l)
        ans = ans & ans1
    return len(ans)

sol1 = 0
sol2 = 0
for g in inp:
    sol1 += count1(g)
    sol2 += count2(g)

print(sol1)
print(sol2)
