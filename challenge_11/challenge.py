"""
--- Day 11: Monkey in the Middle ---
As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then,
one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful
observation, you realize the monkeys operate based on how worried you are about each item.

You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items,
and how the monkey makes decisions based on your worry level. For example:

Monkey 0:
Starting items: 79, 98
Operation: new = old * 19
Test: divisible by 23
If true: throw to monkey 2
If false: throw to monkey 3

Monkey 1:
Starting items: 54, 65, 75, 74
Operation: new = old + 6
Test: divisible by 19
If true: throw to monkey 2
If false: throw to monkey 0

Monkey 2:
Starting items: 79, 60, 97
Operation: new = old * old
Test: divisible by 13
If true: throw to monkey 1
If false: throw to monkey 3

Monkey 3:
Starting items: 74
Operation: new = old + 3
Test: divisible by 17
If true: throw to monkey 0
If false: throw to monkey 1
Each monkey has several attributes:

Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5
means that your worry level after the monkey inspected the item is five times whatever your worry level was 
before inspection.)
Test shows how the monkey uses your worry level to decide where to throw an item next.
If true shows what happens with an item if the Test was true.
If false shows what happens with an item if the Test was false.
After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection
didn't damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the
items it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each 
monkey has had one turn. The process of each monkey taking a single turn is called a round.

When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that
starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a 
monkey is holding no items at the start of its turn, its turn ends.

In the above example, the first round proceeds as follows:

Monkey 0:
Monkey inspects an item with a worry level of 79.
Worry level is multiplied by 19 to 1501.
Monkey gets bored with item. Worry level is divided by 3 to 500.
Current worry level is not divisible by 23.
Item with worry level 500 is thrown to monkey 3.
Monkey inspects an item with a worry level of 98.
Worry level is multiplied by 19 to 1862.
Monkey gets bored with item. Worry level is divided by 3 to 620.
Current worry level is not divisible by 23.
Item with worry level 620 is thrown to monkey 3.
Monkey 1:
Monkey inspects an item with a worry level of 54.
Worry level increases by 6 to 60.
Monkey gets bored with item. Worry level is divided by 3 to 20.
Current worry level is not divisible by 19.
Item with worry level 20 is thrown to monkey 0.
Monkey inspects an item with a worry level of 65.
Worry level increases by 6 to 71.
Monkey gets bored with item. Worry level is divided by 3 to 23.
Current worry level is not divisible by 19.
Item with worry level 23 is thrown to monkey 0.
Monkey inspects an item with a worry level of 75.
Worry level increases by 6 to 81.
Monkey gets bored with item. Worry level is divided by 3 to 27.
Current worry level is not divisible by 19.
Item with worry level 27 is thrown to monkey 0.
Monkey inspects an item with a worry level of 74.
Worry level increases by 6 to 80.
Monkey gets bored with item. Worry level is divided by 3 to 26.
Current worry level is not divisible by 19.
Item with worry level 26 is thrown to monkey 0.
Monkey 2:
Monkey inspects an item with a worry level of 79.
Worry level is multiplied by itself to 6241.
Monkey gets bored with item. Worry level is divided by 3 to 2080.
Current worry level is divisible by 13.
Item with worry level 2080 is thrown to monkey 1.
Monkey inspects an item with a worry level of 60.
Worry level is multiplied by itself to 3600.
Monkey gets bored with item. Worry level is divided by 3 to 1200.
Current worry level is not divisible by 13.
Item with worry level 1200 is thrown to monkey 3.
Monkey inspects an item with a worry level of 97.
Worry level is multiplied by itself to 9409.
Monkey gets bored with item. Worry level is divided by 3 to 3136.
Current worry level is not divisible by 13.
Item with worry level 3136 is thrown to monkey 3.
Monkey 3:
Monkey inspects an item with a worry level of 74.
Worry level increases by 3 to 77.
Monkey gets bored with item. Worry level is divided by 3 to 25.
Current worry level is not divisible by 17.
Item with worry level 25 is thrown to monkey 1.
Monkey inspects an item with a worry level of 500.
Worry level increases by 3 to 503.
Monkey gets bored with item. Worry level is divided by 3 to 167.
Current worry level is not divisible by 17.
Item with worry level 167 is thrown to monkey 1.
Monkey inspects an item with a worry level of 620.
Worry level increases by 3 to 623.
Monkey gets bored with item. Worry level is divided by 3 to 207.
Current worry level is not divisible by 17.
Item with worry level 207 is thrown to monkey 1.
Monkey inspects an item with a worry level of 1200.
Worry level increases by 3 to 1203.
Monkey gets bored with item. Worry level is divided by 3 to 401.
Current worry level is not divisible by 17.
Item with worry level 401 is thrown to monkey 1.
Monkey inspects an item with a worry level of 3136.
Worry level increases by 3 to 3139.
Monkey gets bored with item. Worry level is divided by 3 to 1046.
Current worry level is not divisible by 17.
Item with worry level 1046 is thrown to monkey 1.
After round 1, the monkeys are holding items with these worry levels:

Monkey 0: 20, 23, 27, 26
Monkey 1: 2080, 25, 167, 207, 401, 1046
Monkey 2: 
Monkey 3: 
Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw 
them all before the round ended.

This process continues for a few more rounds:

After round 2, the monkeys are holding items with these worry levels:
Monkey 0: 695, 10, 71, 135, 350
Monkey 1: 43, 49, 58, 55, 362
Monkey 2: 
Monkey 3: 

After round 3, the monkeys are holding items with these worry levels:
Monkey 0: 16, 18, 21, 20, 122
Monkey 1: 1468, 22, 150, 286, 739
Monkey 2: 
Monkey 3: 

After round 4, the monkeys are holding items with these worry levels:
Monkey 0: 491, 9, 52, 97, 248, 34
Monkey 1: 39, 45, 43, 258
Monkey 2: 
Monkey 3: 

After round 5, the monkeys are holding items with these worry levels:
Monkey 0: 15, 17, 16, 88, 1037
Monkey 1: 20, 110, 205, 524, 72
Monkey 2: 
Monkey 3: 

After round 6, the monkeys are holding items with these worry levels:
Monkey 0: 8, 70, 176, 26, 34
Monkey 1: 481, 32, 36, 186, 2190
Monkey 2: 
Monkey 3: 

After round 7, the monkeys are holding items with these worry levels:
Monkey 0: 162, 12, 14, 64, 732, 17
Monkey 1: 148, 372, 55, 72
Monkey 2: 
Monkey 3: 

After round 8, the monkeys are holding items with these worry levels:
Monkey 0: 51, 126, 20, 26, 136
Monkey 1: 343, 26, 30, 1546, 36
Monkey 2: 
Monkey 3: 

After round 9, the monkeys are holding items with these worry levels:
Monkey 0: 116, 10, 12, 517, 14
Monkey 1: 108, 267, 43, 55, 288
Monkey 2: 
Monkey 3: 

After round 10, the monkeys are holding items with these worry levels:
Monkey 0: 91, 16, 20, 98
Monkey 1: 481, 245, 22, 26, 1092, 30
Monkey 2: 
Monkey 3: 

...

After round 15, the monkeys are holding items with these worry levels:
Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
Monkey 1: 110, 36
Monkey 2: 
Monkey 3: 

...

After round 20, the monkeys are holding items with these worry levels:
Monkey 0: 10, 12, 14, 26, 34
Monkey 1: 245, 93, 53, 199, 115
Monkey 2: 
Monkey 3: 
Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you 
want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:

Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
Monkey 3 inspected items 105 times.
In this example, the two most active monkeys inspected items 101 and 105 times. The level of monkey business in this 
situation can be found by multiplying these together: 10605.

58056

--- Part Two ---
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's
inspection didn't damage an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll 
need to find another way to keep your worry levels manageable.

At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.
After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, 
the level of monkey business in this situation is now 2713310158.

15048718170
"""

import re
from collections import defaultdict, Counter
from typing import List, Tuple, NamedTuple, Callable

import math
import operator
import functools


def ints(text: str, sign_prefixes: bool = True) -> Tuple[int, ...]:
    regex = r'([\-+]?\d+)' if sign_prefixes else r'(\d+)'
    return tuple(map(int, re.findall(regex, text)))


class Monkey(NamedTuple):
    id: int
    start_items: Tuple[int]
    op: Callable[[int], int]
    div_by: int
    if_true: int
    if_false: int


def main(text: str):
    monkeys, p = parse_monkeys(text)
    print('Part 1:', simulate(monkeys, p, True))
    print('Part 2:', simulate(monkeys, p, False))


def simulate(monkeys: List[Monkey], p: int, part1: bool) -> int:
    # Part 1 simulates 20 rounds, and divides the stress by 3 each time
    # Part 2 simulates 10k rounds, and without dividing by three this quickly (i.e. within ~100 rounds), reaches numbers with >1k digits... and asks you to square them.
    # This is clearly infeasible, even for python. So, we have to be clever
    # Since we only ever check the divisibility of a given stress level, and we do basic add + multiply operations (which are functional operations mod p)
    # We can translate each stress level to a tuple of stresses mod p, where p = the product of all monkey's divisors

    inspects = Counter()
    monkey_items = [list(monkey.start_items) for monkey in monkeys]
    total_rounds = 20 if part1 else 10_000
    for _ in range(total_rounds):
        for monkey, items in zip(monkeys, monkey_items):
            for item in items:
                inspects[monkey.id] += 1
                next_item = monkey.op(item)
                if part1:
                    next_item //= 3
                else:
                    next_item %= p
                next_monkey = monkey.if_true if (
                    next_item % monkey.div_by) == 0 else monkey.if_false
                monkey_items[next_monkey].append(next_item)
            items.clear()

    (_, a), (_, b), *_ = inspects.most_common(2)
    return a * b


def parse_monkeys(text: str) -> Tuple[List[Monkey], int]:
    monkeys = []
    monkey_items = []
    for i, part in enumerate(text.split('\n\n')):
        _, start, op, test, if_true, if_false = [
            x.strip() for x in part.split('\n')]
        start = ints(start)
        div_by = ints(test)[0]
        if_true = ints(if_true)[0]
        if_false = ints(if_false)[0]

        # Very primitive expression parsing
        lhs, op_char, rhs = op.split(' = ')[1].split(' ')
        is_square = rhs == 'old'
        value = 0 if is_square else int(rhs)
        op_par = functools.partial(
            operator.mul if op_char == '*' else operator.add, value)

        monkeys.append(
            Monkey(i, start, square if is_square else op_par, div_by, if_true, if_false))
        monkey_items.append(start)

    # For part 2, instead of representing the monkey's items as a single integer,
    # We represent each monkey's value as the tuple of integers, modulo each other monkey's value
    p = math.prod(m.div_by for m in monkeys)
    return monkeys, p


def square(old: int) -> int:
    return old * old


def main_original(text: str):
    """
    This was the leaderboard-state main
    As you can see, I didn't separate part 1 and 2, and hardcoded part of the input
    """

    OPS = [
        lambda o: o * 13,
        lambda o: o * o,
        lambda o: o + 6,
        lambda o: o + 2,
        lambda o: o + 3,
        lambda o: o + 4,
        lambda o: o + 8,
        lambda o: o * 7
    ]

    TOPS = [
        lambda o: o * 19,
        lambda o: o + 6,
        lambda o: o * o,
        lambda o: o + 3
    ]

    # OPS = TOPS

    monkeys = []
    for i, part in enumerate(text.split('\n\n')):
        _, start, op, test, if_true, if_false = [
            x.strip() for x in part.split('\n')]
        start = ints(start)
        op = OPS[i]
        div_by = ints(test)[0]
        if_false = ints(if_false)[0]
        if_true = ints(if_true)[0]

        monkeys.append([list(start), op, div_by, if_true, if_false])
    print(monkeys)

    divs = sorted([m[2] for m in monkeys])

    def to_divs(n: int):
        return tuple(n % d for d in divs)

    for i in range(len(monkeys)):
        monkeys[i][0] = [to_divs(n) for n in monkeys[i][0]]
        print(monkeys[i][0])

    inspects = defaultdict(int)
    for _ in range(10000):
        mi = 0
        for items, op, div_by, if_true, if_false in monkeys:
            for item in items:
                inspects[mi] += 1
                # new_item = op(item)# // 3
                new_item = tuple(op(p) % dv for p, dv in zip(item, divs))
                if new_item[divs.index(div_by)] == 0:
                    monkeys[if_true][0].append(new_item)
                else:
                    monkeys[if_false][0].append(new_item)
            monkeys[mi][0] = []
            mi += 1
    print(sorted(inspects.values()))


if __name__ == '__main__':
    with open("challenge_11/input.txt") as f:
        main(f.read())
