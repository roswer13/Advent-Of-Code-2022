"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the
number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs
(5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

843

"""


def get_data() -> list:
    with open("challenge_4/data.txt", "r") as file:
        data = file.read()
        return data.split("\n")


def partial_overlap(pair):
    return ((pair[0][0] <= pair[1][0] <= pair[0][1]) or (pair[1][0] <= pair[0][0] <= pair[1][1]))


def boundaries(pair_data):
    return tuple(tuple(int(elem)for elem in pair.split("-")) for pair in pair_data.strip().split(","))


def total_contained(pair_assignments):
    return sum(partial_overlap(boundaries(pair)) for pair in pair_assignments)


print(total_contained(pair_assignments=get_data()))
