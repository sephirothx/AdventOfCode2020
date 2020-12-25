key = 13316116
door = 13651422

def trans(n,ls):
    value = 1
    for _ in range(ls):
        value *= n
        value %= 20201227
    return value

i = 1
ls = 0
while i not in [key, door]:
    ls += 1
    i *= 7
    i %= 20201227
    if i in (key, door):
        print(trans(door if i==key else key, ls))
