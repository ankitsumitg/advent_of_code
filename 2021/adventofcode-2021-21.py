from functools import lru_cache
from itertools import product

p1_start_position = 10 - 1
p2_start_position = 7 - 1
board = list(range(1, 11))


def solve1(p1_start_pos, p2_start_pos):
    p1_score = 0
    p2_score = 0
    dice = list(range(1, 101))
    dice_start_pos = 0
    no_times_dice_rolled = 0
    while True:
        p1_start_pos = (dice[dice_start_pos % 100] + dice[(dice_start_pos + 1) % 100] + dice[
            (dice_start_pos + 2) % 100] + p1_start_pos) % 10
        p1_score += board[p1_start_pos]
        no_times_dice_rolled += 3
        dice_start_pos += 3
        if p1_score >= 1000:
            break
        p2_start_pos = (dice[dice_start_pos % 100] + dice[(dice_start_pos + 1) % 100] + dice[
            (dice_start_pos + 2) % 100] + p2_start_pos) % 10
        p2_score += board[p2_start_pos]
        no_times_dice_rolled += 3
        dice_start_pos += 3
        if p2_score >= 1000:
            break
    print(f'Part 1 : {p1_score * no_times_dice_rolled if p1_score < p2_score else p2_score * no_times_dice_rolled}')


@lru_cache(maxsize=None)
def solve2(p1_start_pos, p2_start_pos, score1=0, score2=0):
    if score2 >= 21:
        return 0, 1
    if score1 >= 21:
        return 1, 0
    wins1, wins2 = 0, 0
    for u1, u2, u3 in product([1, 2, 3], repeat=3):
        pos1_new = (p1_start_pos + u1 + u2 + u3) % 10
        ans1, ans2 = solve2(p2_start_pos, pos1_new, score2, score1 + pos1_new + 1)
        wins1, wins2 = wins1 + ans2, wins2 + ans1
    return wins1, wins2


solve1(p1_start_position, p2_start_position)
print(f'Part 2 : {max(solve2(p1_start_position, p2_start_position))}')
