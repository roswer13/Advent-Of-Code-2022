"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying
the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the
top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they
still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf
(with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these
three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""

def get_data() -> list:
    with open("challenge_1\data.txt", "r") as file:
        data = file.read()
        data = data.split("\n\n")

        return data


def sum_calories(calories_list: list) -> int:
    calories = []

    for calorie in calories_list:
        calorie = calorie.split("\n")
        calorie = [int(c) for c in calorie]
        calorie = sum(calorie)

        calories.append(calorie)

    calories.sort(reverse=True)
    return sum(calories[:3])


print(sum_calories(calories_list=get_data()))