"""
--- Part Two ---
Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list of received packets.

The distress signal protocol also requires that you include two additional divider packets:

[[2]]
[[6]]
Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two 
divider packets - into the correct order.

For the example above, the result of putting the packets in the correct order is:

[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]

Afterward, locate the divider packets. To find the decoder key for this distress signal, you need to determine the indices of 
the two divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) 
In this example, the divider packets are 10th and 14th, and so the decoder key is 140.

21890
"""

from functools import cmp_to_key

with open("challenge_13/input.txt") as fin:
    parts = fin.read().strip().replace("\n\n", "\n").split("\n")


def compare(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]

    if isinstance(a, int) and isinstance(b, list):
        a = [a]

    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a == b:
            return 0
        return -1

    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            x = compare(a[i], b[i])
            if x == 1:
                return 1
            if x == -1:
                return -1

            i += 1

        if i == len(a):
            if len(a) == len(b):
                return 0
            return 1  # a ended first

        # If i didn't hit the end of a, it hit the end of b first
        #   This means that b is shorter, which is bad
        return -1


lists = list(map(eval, parts))
lists.append([[2]])
lists.append([[6]])
lists = sorted(lists, key=cmp_to_key(compare), reverse=True)


for i, li in enumerate(lists):
    if li == [[2]]:
        a = i + 1
    if li == [[6]]:
        b = i + 1

print(a * b)
