UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

DIR = {
    UP: (0, 1),
    DOWN: (0, -1),
    LEFT: (-1, 0),
    RIGHT: (1, 0)
}

def manhattan(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
