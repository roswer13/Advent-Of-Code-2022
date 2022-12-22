"""
--- Day 22: Monkey Map ---
The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly 
the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a force field. To pass through the 
force field, you have to enter a password; doing so involves tracing a specific path on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
The first half of the monkeys' notes is a map of the board. It is comprised of a set of open tiles (on 
which you can move, drawn .) and solid walls (tiles which you cannot enter, drawn #).

The second half is a description of the path you must follow. It consists of alternating numbers and letters:

A number indicates the number of tiles to move in the direction you are facing. If you run into a wall, you 
stop moving forward and continue with the next instruction.
A letter indicates whether to turn 90 degrees clockwise (R) or counterclockwise (L). Turning happens 
in-place; it does not change your current tile.
So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the 
right (from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you wrap around to the other side of the board. In 
other words, if your next tile is off of the board, you should instead look in the direction opposite of your 
current facing as far as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at A and facing to the right, the tile in front of you is marked B; if you are at C 
and facing down, the tile in front of you is marked D:

        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.
It is possible for the next tile (after wrapping around) to be a wall; this still counts as there being a 
wall in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the last facing you had with an arrow on each tile you visit, the full path taken by the above 
example looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#...v..v#    
>>>v...>#.>>    
..#v...#....    
...>>>>v..#.    
        ...#....
        .....#..
        .#......
        ......#.
To finish providing the password to this strange input device, you need to determine numbers for your 
final row, column, and facing as your final position appears from the perspective of the original 
map. Rows start from 1 at the top and count downward; columns start from 1 at the left and count 
rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in 
the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). The 
final password is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is 6, the final column is 8, and the final facing is 0. So, the 
final password is 1000 * 6 + 4 * 8 + 0: 6032.

43466

--- Part Two ---
As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange input device, but it isn't quite what the monkeys drew in their notes. Instead, you 
are met with a large cube; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map does have six 50x50 regions on it. If you were to carefully fold the map, you 
should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666
You still start in the same position and with the same facing as before, but the wrapping rules are different. Now, if you would walk off the board, you instead proceed around the cube. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

        ...#
        .#..
        #...
        ....
...#.......#
........#..A
..#....#....
.D........#.
        ...#..B.
        .....#..
        .#......
        ..C...#.
Walls still block your path, even if they are on a different face of the cube. If you are at E facing 
up, your movement is blocked by the wall marked by the arrow:

        ...#
        .#..
     -->#...
        ....
...#..E....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
Using the same method of drawing the last facing you had with an arrow on each tile you visit, the 
full path taken by the above example now looks like this:

        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#..^...v#    
.>>>>>^.#.>>    
.^#....#....    
.^........#.    
        ...#..v.
        .....#v.
        .#v<<<<.
        ..v...#.
The final password is still calculated from your final position and facing from the perspective of the 
map. In this example, the final row is 5, the final column is 7, and the final facing is 3, so the final
password is 1000 * 5 + 4 * 7 + 3 = 5031.

162155

"""

import re
L = -1j
R = 1j
with open("2022/challenge_22/input.txt") as file:
    raw_map, raw_instructions = file.read().split("\n\n")
instructions = re.findall(r"(\d+|R|L)", raw_instructions)
empties = set()
walls = set()
portals = {}
for y, row in enumerate(raw_map.splitlines(), 1):
    for x, c in enumerate(row, 1):
        if c == "#":
            walls.add(complex(x, y))
        elif c == ".":
            empties.add(complex(x, y))
on_map = empties | walls
num_rows = max(int(z.imag) for z in on_map)
num_cols = max(int(z.real) for z in on_map)
for x in range(1, num_cols+1):
    for y in range(-1, num_rows+2):
        if complex(x, y) not in on_map and complex(x, y+1) in on_map:
            start = complex(x, y)
        if complex(x, y) not in on_map and complex(x, y-1) in on_map:
            portals[start, -1j] = complex(x, y-1)
            portals[complex(x, y), 1j] = start+1j
            break

for y in range(1, num_rows+1):
    for x in range(-1, num_cols+2):
        if complex(x, y) not in on_map and complex(x+1, y) in on_map:
            start = complex(x, y)
        if complex(x, y) not in on_map and complex(x-1, y) in on_map:
            portals[start, -1] = complex(x-1, y)
            portals[complex(x, y), 1] = start+1
            break
d = d0 = 1  # Right
p = p0 = min(empties, key=lambda z: (z.imag, z.real))

for ins in instructions:
    if ins == 'L':
        d *= L
    elif ins == 'R':
        d *= R
    else:
        for _ in range(int(ins)):
            n = p+d
            if n not in on_map:
                n = portals[n, d]
            if n in walls:
                break
            assert n in empties
            p = n

print("Part 1:", int(1000*p.imag+4*p.real+(1, 1j, -1, -1j).index(d)))

cube_portals = dict((  # Some of these are backwards!
    *(((complex(50+i,  0), -1j), (complex(1, 150+i), 1))
      for i in range(1, 51)),  # A 2 1 ^
    *(((complex(0, 150+i), -1), (complex(50+i,  1), 1j))
      for i in range(1, 51)),  # B 1 4 <
    *(((complex(100+i,  0), -1j), (complex(i, 200), -1j))
      for i in range(1, 51)),  # C 3 1 ^
    *(((complex(i, 201), 1j), (complex(100+i,  1), 1j))
      for i in range(1, 51)),  # D 1 4 v
    *(((complex(50,    i), -1), (complex(1, 151-i), 1))
      for i in range(1, 51)),  # E 2 1 < OP
    *(((complex(0, 100+i), -1), (complex(51, 51-i), 1))
      for i in range(1, 51)),  # F 1 3 < OP
    *(((complex(50, 50+i), -1), (complex(i, 101), 1j))
      for i in range(1, 51)),  # G 2 2 <
    *(((complex(i, 100), -1j), (complex(51, 50+i), 1))
      for i in range(1, 51)),  # H 1 3 ^
    *(((complex(151,    i), 1), (complex(100, 151-i), -1))
      for i in range(1, 51)),  # I 3 1 > OP
    *(((complex(101, 100+i), 1), (complex(150, 51-i), -1))
      for i in range(1, 51)),  # J 2 3 > OP
    *(((complex(100+i, 51), 1j), (complex(100, 50+i), -1))
      for i in range(1, 51)),  # K 3 1 v
    *(((complex(101, 50+i), 1), (complex(100+i, 50), -1j))
      for i in range(1, 51)),  # L 2 2 >
    *(((complex(50+i, 151), 1j), (complex(50, 150+i), -1))
      for i in range(1, 51)),  # M 2 3 v
    *(((complex(51, 150+i), 1), (complex(50+i, 150), -1j))
      for i in range(1, 51)),  # N 1 4 >
))
count = 0
for (source, sd), (dest, dd) in cube_portals.items():
    if count % 50 == 0:
        print(end=chr(ord('A')+count//50))
    assert source not in on_map
    assert source-sd in on_map
    assert source-50*sd in on_map
    assert dest in on_map
    assert dest+49*dd in on_map
    assert dest-dd not in on_map
    assert cube_portals[dest-dd, -dd] == (source-sd, -sd)
    count += 1
assert count == 14*50
assert len(set(cube_portals.values())) == len(cube_portals)
print("\nAssertions passed")

d = d0
p = p0
for ins in instructions:
    if ins == 'L':
        d *= L
    elif ins == 'R':
        d *= R
    else:
        for _ in range(int(ins)):
            np = p+d
            nd = d
            if np not in on_map:
                np, nd = cube_portals[np, d]
                assert np-nd not in on_map
            if np in walls:
                break
            assert np in empties
            p = np
            d = nd
print("Part 2:", int(1000*p.imag+4*p.real+(1, 1j, -1, -1j).index(d)))
