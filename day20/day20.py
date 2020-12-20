import numpy as np
import math as m
import copy
import re
inp = open('input.txt').read().split('\n\n')
SIZE = int(m.sqrt(len(inp)))

tiles = {}
for tile in inp:
    tile = tile.splitlines()
    n = re.findall(r'\d+', tile[0])[0]
    tiles[int(n)] = np.array([[x for x in y] for y in tile[1:]])

def matchlr(tl, tr):
    c0, c1 = tl[:,-1], tr[:,0]
    return all(c0==c1)

def matchud(tu, td):
    r0, r1 = tu[-1], td[0]
    return all(r0==r1)

def get_transforms(t):
    for i in range(4):
        tmp = np.rot90(t, i)
        yield tmp
        yield np.flipud(tmp)

def arrange(n=0, used=set(), pic={}, sol={}):
    if n == SIZE*SIZE:
        return pic, sol
    x, y = n%SIZE, n//SIZE
    for i, tile in tiles.items():
        if i in used:
            continue
        for t in get_transforms(tile):
            lr = matchlr(pic[(x-1, y)], t) if x>0 else True
            ud = matchud(pic[(x, y-1)], t) if y>0 else True
            if lr and ud:
                c = copy.deepcopy(pic)
                u = used.copy()
                s = sol.copy()
                c[(x,y)] = t
                u.add(i)
                s[(x,y)] = i
                ret = arrange(n+1, u, c, s)
                if ret:
                    return ret
    return None

def monsters(picture):
    ret = 0
    for y in range(len(picture) - len(monster) + 1):
        for x in range(len(picture[0]) - len(monster[0]) + 1):
            found = True
            for i, part in enumerate(monster):
                for j in range(len(part)):
                    if part[j] == '#' and picture[y+i,x+j] != '#':
                        found = False
                        break
                if not found:
                    break
            if found:
                ret += 1
    return ret

pic, sol = arrange()
print(sol[(0,0)] *
      sol[(0,SIZE-1)] *
      sol[(SIZE-1,0)] *
      sol[(SIZE-1,SIZE-1)])

monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]
mhash = sum(l.count('#') for l in monster)

PER = len(pic[(0,0)]) - 2

final = np.empty(shape=(SIZE*PER,SIZE*PER), dtype=str)
for x,y in pic:
    final[PER*y:PER*y + PER, PER*x:PER*x + PER] = pic[(x,y)][1:-1,1:-1].copy()

hashes = np.count_nonzero(final == '#')
for p in get_transforms(final):
    m = monsters(p)
    if m != 0:
        print(hashes - mhash*m)
        break
