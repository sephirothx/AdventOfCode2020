inp = open('input.txt').read().splitlines()
d = {
    "e": (1,0),
    "se": (1,-1),
    "sw": (0,-1),
    "w": (-1,0),
    "nw": (-1,1),
    "ne": (0,1)
}

tiles = set()
def move(s):
    def nextdir(s,i):
        if s[i] in 'ew':
            return s[i], i+1
        else:
            return s[i]+s[i+1], i+2
    pos = [0,0]
    i = 0
    while i < len(s):
        c, i = nextdir(s,i)
        pos[0] += d[c][0]
        pos[1] += d[c][1]
    return (pos[0], pos[1])

for l in inp:
    t = move(l)
    if t in tiles:
        tiles.remove(t)
    else:
        tiles.add(t)
print(len(tiles))

def conway(t):
    def get_neighbors(tile):
        for di in d.values():
            yield (tile[0]+di[0], tile[1]+di[1])
    new_t = set()
    space = set()
    for tile in t:
        space.add(tile)
        for n in get_neighbors(tile):
            space.add(n)
    for tile in space:
        bn = 0
        for n in get_neighbors(tile):
            if n in t:
                bn += 1
        if tile in t and bn==1 or bn==2:
            new_t.add(tile)
        elif tile not in t and bn==2:
            new_t.add(tile)
    return new_t

for _ in range(100):
    tiles = conway(tiles)
    print(len(tiles))
