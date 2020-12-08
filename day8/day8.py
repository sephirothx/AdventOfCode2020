inp = open('input.txt').read().splitlines()

instr = []
for l in inp:
    op, v = l.split()
    v = int(v)
    instr.append((op, v))

def run(code):
    acc = 0
    ip = 0
    seen = set()
    while ip < len(code):
        if ip in seen:
            break
        seen.add(ip)
        op, v = code[ip]
        if op == "nop":
            ip += 1
        elif op == "acc":
            acc += v
            ip += 1
        elif op == "jmp":
            ip += v
    return acc, ip

print(run(instr)[0])
sol2 = 0
for i, (op, v) in enumerate(instr):
    if op == 'acc':
        continue
    tmp = instr.copy()
    if op == 'nop':
        tmp[i] = ('jmp', v)
    elif op == 'jmp':
        tmp[i] = ('nop', v)
    acc, ip = run(tmp)
    if ip == len(tmp):
        print(acc)
