"""
--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above 
broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation,
b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). 
Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly
one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square 
can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step 
to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than 
the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually 
you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). 
The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

412

--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't 
very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square
marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find 
the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at 
elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.

402
"""
from sys import stdin
import re


def pos_gi(line):
    return list(map(int, re.findall(r"\d+", line)))


def gi(line):
    # (?:(?<!\d)-)?\d+
    return list(map(int, re.findall(r"-?\d+", line)))


def GI(line):
    return int(re.findall(r"-?\d+", line)[0])


def gf(line):
    return list(map(float, re.findall(r"-?\d+(?:\.\d+)?", line)))


def pos_gf(line):
    return list(map(float, re.findall(r"\d+(?:\.\d+)?", line)))


def gs(line):
    return re.findall(r"[a-zA-Z]+", line)


def neigh4(x, y, H, W):
    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)


def neigh8(x, y, H, W):
    for nx, ny in (x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)


OUTPUT = 1
if OUTPUT:
    file = open("challenge_12/input.txt", "r")
    input = [i.strip() for i in file.readlines()]
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]


grid = input[:]
H = len(grid)
W = len(grid[0])


def is_good(a, b):
    return ord(b.replace("E", "z")) - ord(a.replace("S", "a")) <= 1


for src_char in "S", "Sa":  # Part 1, then 2
    queue = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] in src_char:
                queue.append((0, i, j))
    # breadh-first search for shortest path
    seen = set()
    for m, x, y in queue:
        if grid[x][y] == "E":
            print(m)
            break
        for nx, ny in neigh4(x, y, H, W):
            if is_good(grid[x][y], grid[nx][ny]) and (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append((m + 1, nx, ny))
