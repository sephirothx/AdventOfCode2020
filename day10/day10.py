from math import prod
inp = sorted([int(x) for x in open('input.txt').read().splitlines()])
inp.append(inp[-1] + 3)

prev = 0
diff1 = 0
diff3 = 0
groups_diff1 = []
consecutive = 1
for i in inp:
    if i - prev == 1:
        diff1 +=1
        consecutive += 1
    elif i - prev == 3:
        diff3 += 1
        if consecutive > 1:
            groups_diff1.append(consecutive)
            consecutive = 1
    prev = i
print(diff1 * diff3)

def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

print(prod([tribonacci(n) for n in groups_diff1]))
