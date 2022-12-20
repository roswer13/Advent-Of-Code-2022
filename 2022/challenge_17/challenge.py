"""
--- Day 17: Pyroclastic Flow ---
Your handheld device has located an alternative exit from the cave for you and the elephants. 
The ground is rumbling almost continuously now, but the strange valves bought you some time. It's 
definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are 
falling into the chamber from above, presumably due to all the rumbling. If you can't work out 
where the rocks will fall next, you might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the 
end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls 
themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they 
fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
In jet patterns, < means a push to the left, while > means a push to the right. The pattern above 
means that the jets will push a falling rock right, then right, then right, then left, then left, 
then right, and so on. If the end of the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is 
two units away from the left wall and its bottom edge is three units above the highest rock in the 
room (or the floor, if there isn't one).

After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the 
direction indicated by the next symbol in the jet pattern) and then falling one unit down. If 
any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, 
the movement instead does not occur. If a downward movement would have caused a falling rock to 
move into the floor or an already-fallen rock, the falling rock stops where it is (having landed 
on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+
The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+
To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 
2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks 
will be 3068 units tall.

3181

--- Part Two ---
The elephants are not impressed by your simulation. They demand to know how tall the tower will be 
after 1000000000000 rocks have stopped! Only then will they feel confident enough to proceed through the cave.

In the example above, the tower would be 1514285714288 units tall!

1570434782634
"""

from itertools import cycle
from collections import defaultdict

inp = cycle(enumerate(open("2022/challenge_17/input.txt").read()))
rocks = cycle(  # rows of bits
    enumerate([[120], [32, 112, 32], [112, 16, 16], [64, 64, 64, 64], [96, 96]])
)
M = []  # map
S = []  # sequence of positions of rocks at rest
R = defaultdict(list)  # (rock_idx, instruction_idx) -> S_idx
H = []  # sequence of max heights
L = C = Z = 0  # prefix, cycle length and height per cycle


def fits(rk, x, y):
    return not any(
        M[j] & rk[j - y] >> x for j in range(y, min(len(M), y + len(rk)))
    ) and all(r >> x << x == r for r in rk)


while not C:
    ri, rock = next(rocks)
    x, y = 2, len(M) + 4
    # play rock
    while y and fits(rock, x, y - 1):
        y -= 1
        ai, arrow = next(inp)
        nx = max(0, x - 1) if arrow == "<" else min(7, x + 1)
        x = nx if fits(rock, nx, y) else x

    # update map
    for j, r in enumerate(rock, y):
        if j < len(M):
            M[j] |= r >> x
        else:
            M.append(r >> x)
    H.append(len(M))
    S.append(x)

    # find cycle
    R[(ri, ai)].append(len(S))
    for i, m in enumerate(R[(ri, ai)][:-1]):
        for b in R[(ri, ai)][:i]:
            if m - b == len(S) - m and S[b:m] == S[m:]:
                L, C, Z = m, m - b, len(M) - H[m-1]


def height(iters): return (Z * ((iters - L) // C) + H[L+((iters - L) % C)-1])


print("Part1: ", height(2022))
print("Part1: ", height(1000000000000))
