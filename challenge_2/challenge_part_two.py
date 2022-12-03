"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how
the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z
means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose
so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y),
so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a
score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes
exactly according to your strategy guide?
"""

def get_data() -> list:
    with open("challenge_2/data.txt", "r") as file:
        data = file.read()
        return data.split("\n")

def get_score(rounds: list) -> int:
    score = 0

    for _round in rounds:
        _round = _round.split(" ")

        opponent = _round[0]
        player = _round[1]

        if opponent == "A": #  1
            if player == "X":
                score += 3
                score += 0
            elif player == "Y":
                score += 1
                score += 3
            elif player == "Z":
                score += 2
                score += 6

        elif opponent == "B": #  2
            if player == "X":
                score += 1
                score += 0
            elif player == "Y":
                score += 2
                score += 3
            elif player == "Z":
                score += 3
                score += 6
                
        elif opponent == "C":  #  3
            if player == "X":
                score += 2
                score += 0
            elif player == "Y":
                score += 3
                score += 3
            elif player == "Z":
                score += 1
                score += 6

    return score


print(get_score(rounds=get_data()))