inp = open('input.txt').readlines()

def count(dx, dy):
    x = 0
    ret = 0
    for i in range(0, len(inp), dy):
        s = inp[i].strip()  # apparently readlines does not strip :(
        if s[x % len(s)] == '#':
            ret += 1
        x += dx
    return ret

print(count(3,1))
print(count(1,1) *
      count(3,1) *
      count(5,1) *
      count(7,1) *
      count(1,2))
