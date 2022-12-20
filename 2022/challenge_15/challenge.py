"""
--- Day 15: Beacon Exclusion Zone ---
You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels.
You don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors 
that you imagine were originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough 
to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, 
hit the big button on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and
begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer 
coordinates. Each sensor knows its own position and can determine the position of a beacon precisely; 
however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan 
distance. (There is never a tie where two beacons are the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon 
to it is at 10,16.

Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only 
identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that
close or closer to that sensor. There could still be beacons that just happen to not be the closest 
beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

None of the detected beacons seem to be producing the distress signal, so you'll need to work out where 
the distress beacon is by working out where it isn't. For now, keep things simple by counting the positions
where a beacon cannot possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row 
where y=10, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from 
all sensors near that row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.
In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions 
cannot contain a beacon?

4737567.

--- Part Two ---
Your handheld device indicates that the distress signal is coming from a beacon nearby. The 
distress beacon is not detected by any sensor, but the distress beacon must have x and y 
coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which 
can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each 
be at most 20. With this reduced search area, there is only a single position that could have 
a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

13267474686239
"""

import re
from typing import List, Optional, Set, Tuple, Union


def input_reader(f: str) -> List[List[Tuple[int, int]]]:
    with open(f, "r", encoding="utf-8") as f:
        sensors = []
        for line in f.readlines():
            coords = list(map(int, re.findall(r"=(-?\d+)", line)))
            sensors.append(list(zip(coords[::2], coords[1::2])))
    return sensors


def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    return abs(p1_x - p2_x) + abs(p1_y - p2_y)


def interval_covering(
    start: int, stop: int, sorted_intervals: List[Tuple[int, int]], max_dim: int
) -> int:
    for covering_interval in sorted_intervals:
        if stop >= max_dim:
            return max_dim - (stop + 1)
        if stop + 1 < covering_interval[0]:
            return stop + 1
        if (interval_right := covering_interval[1]) > stop:
            stop = interval_right
    return -1


def row_inspector(
    sensors: List[List[Tuple[int, int]]], row: int, max_dim: Optional[int] = None
) -> Union[int, Set[int]]:
    def sensor_coverage(
        sensor_coord: Tuple[int, int], beacon_coord: Tuple[int, int]
    ) -> Set[Tuple[int, int]]:
        max_dist = manhattan_distance(sensor_coord, beacon_coord)
        sensor_coord_x, sensor_coord_y = sensor_coord
        beacon_coord_x, beacon_coord_y = beacon_coord
        surrounding_coords = set()
        if abs(row - sensor_coord_y) <= max_dist:
            x_dof = max_dist - abs(row - sensor_coord_y)
            if max_dim is None:
                for dx in range(-x_dof, x_dof + 1):
                    surrounding_coords.add((sensor_coord_x + dx))
            else:
                surrounding_coords.add(
                    (sensor_coord_x - x_dof, sensor_coord_x + x_dof))
        return surrounding_coords

    total_coverage, known_beacon_locs = set(), set()
    for sensor_coord, beacon_coord in sensors:
        beacon_coord_x, beacon_coord_y = beacon_coord
        total_coverage |= sensor_coverage(sensor_coord, beacon_coord)
        if beacon_coord_y == row:
            known_beacon_locs.add(beacon_coord_x)

    if max_dim is None:
        return len(total_coverage - known_beacon_locs)
    else:
        return interval_covering(
            -1, -1, sorted(total_coverage,
                           key=lambda t: (t[0], -t[1])), max_dim
        )


def distress_beacon_freq(sensors: List[List[Tuple[int, int]]], max_dim: int) -> int:
    for row in range(max_dim + 1):
        if (distress_beacon_x := row_inspector(sensors, row, max_dim)) >= 0:
            return 4_000_000 * distress_beacon_x + row


def main():
    DATA = input_reader("2022/challenge_15/input.txt")
    print(row_inspector(DATA, 2_000_000))  # 6275922
    print(distress_beacon_freq(DATA, 4_000_000))  # 11747175442119


if __name__ == "__main__":
    main()
