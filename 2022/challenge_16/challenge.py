"""
--- Day 16: Proboscidea Volcanium ---
The sensors have led you to the origin of the distress signal: yet another handheld device, 
just like the one the Elves gave you. However, you don't see any Elves around; instead, the 
device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the 
elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan 
the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of 
pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes 
before the volcano erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release valves. 
You aren't sure how such a system got into a volcano, but you don't have time to complain; your 
device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure 
per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled AA. You 
estimate it will take you one minute to open a single valve and one minute to follow any tunnel 
from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or 
something: its flow rate is 0, so there's no point in opening it. However, you could spend one 
minute moving to valve BB and another minute opening it; doing so would release pressure during 
the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. 
Then, you could spend your third minute moving to valve CC and your fourth minute opening it, 
providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total 
pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or all of the valves 
by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, 
so you'll need to be methodical. Instead, consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

2124

--- Part Two ---
You're worried that even with an optimal approach, the pressure released won't be enough. What if you 
got one of the elephants to help you?

It would take you 4 minutes to teach an elephant how to open the right valves in the right order, 
leaving you with only 26 minutes to actually execute your plan. Would having two of you working 
together be better, even if it means having less time? (Assume that you teach the elephant before 
opening any valves yourself, giving you both the same full 26 minutes.)

In the example above, you could teach the elephant to help you as follows:

== Minute 1 ==
No valves are open.
You move to valve II.
The elephant moves to valve DD.

== Minute 2 ==
No valves are open.
You move to valve JJ.
The elephant opens valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You open valve JJ.
The elephant moves to valve EE.

== Minute 4 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve II.
The elephant moves to valve FF.

== Minute 5 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve AA.
The elephant moves to valve GG.

== Minute 6 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve BB.
The elephant moves to valve HH.

== Minute 7 ==
Valves DD and JJ are open, releasing 41 pressure.
You open valve BB.
The elephant opens valve HH.

== Minute 8 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve CC.
The elephant moves to valve GG.

== Minute 9 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve CC.
The elephant moves to valve FF.

== Minute 10 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant moves to valve EE.

== Minute 11 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant opens valve EE.

(At this point, all valves are open.)

== Minute 12 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 20 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
With the elephant helping, after 26 minutes, the best you could do would release a total of 1707 pressure.

2775

"""
from collections import namedtuple
from itertools import combinations

Valve = namedtuple("Valve", ("name", "rate", "destinations"))

valves = {}
shortest_paths = {}


def explore(start: Valve, unvisited, turns=0, rate=0, flow=0, path=None, max_turns=30, paths=None):
    if len(unvisited) == 0:
        flow += (max_turns - turns) * rate
        paths.append((path, flow))
        return flow
    for v in unvisited:
        # travel then open valve
        new_turns = shortest_paths.get(key(start.name, v.name), 0) + 1
        if new_turns == 1 or turns + new_turns > max_turns:
            new_flow = (max_turns - turns) * rate
            paths.append((path, flow + new_flow))
            continue
        new_flow = rate * new_turns
        explore(v, unvisited=unvisited - {v}, turns=turns + new_turns, rate=rate + v.rate,
                flow=flow+new_flow, path=path + [v.name], max_turns=max_turns, paths=paths)


def key(a, b):
    return tuple(sorted([a, b]))


def best(paths):
    max_flow = (None, 0)
    for p in paths:
        if p[1] > max_flow[1]:
            max_flow = p
    return max_flow


def main():
    with open("2022/challenge_16/input.txt") as fh:
        lines = [line.strip() for line in fh.readlines()]
    for line in lines:
        v, t = line.split("; ")
        s = v.split()[1]
        r = int(v.split("=")[1])
        t = [d[:2] for d in t.split()[4:]]
        for d in t:
            shortest_paths[key(s, d)] = 1
            new_paths = {}
            for p, l in shortest_paths.items():
                if d == p[0] and p[1] != s:
                    k = key(p[1], s)
                elif d == p[1] and p[0] != s:
                    k = key(p[0], s)
                else:
                    continue
                if k not in shortest_paths or l + 1 < shortest_paths[k]:
                    new_paths[k] = l + 1
            shortest_paths.update(new_paths)
        valves[s] = Valve(s, r, tuple(t))
    unvisited = {v for v in valves.values() if v.rate != 0}
    paths = []
    explore(valves["AA"], unvisited=unvisited,
            path=[], max_turns=30, paths=paths)
    print("part 1", best(paths))

    max_flow = (None, None, 0)
    for i in range(len(valves)):
        for c in combinations(unvisited, i):
            s1 = set(c)
            s2 = unvisited - s1
            paths = []
            explore(valves["AA"], unvisited=s1,
                    path=[], max_turns=26, paths=paths)
            b1 = best(paths)
            paths = []
            explore(valves["AA"], unvisited=s2,
                    path=[], max_turns=26, paths=paths)
            b2 = best(paths)
            if b1[1] + b2[1] > max_flow[2]:
                max_flow = (b1, b2, b1[1] + b2[1])
    print("part 2", max_flow)


main()
