from functools import reduce
from itertools import permutations
from math import ceil

with open('input18', 'r') as f:
    snail_nums_list = [eval(i) for i in f.read().splitlines()]


def add_to_where(x, n, on):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    if on == 'left':
        return [add_to_where(x[0], n, 'left'), x[1]]
    return [x[0], add_to_where(x[1], n, 'right')]


def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, a, right = explode(a, n - 1)
    if exp:
        return True, left, [a, add_to_where(b, right, 'left')], None
    exp, left, b, right = explode(b, n - 1)
    if exp:
        return True, None, [add_to_where(a, left, 'right'), b], right
    return False, None, x, None


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, ceil(x / 2)]
        return False, x
    a, b = x
    to_check, a = split(a)
    if to_check:
        return True, [a, b]
    to_check, b = split(b)
    return to_check, [a, b]


def sum_snail_nums(num1, num2):
    final = [num1, num2]
    while True:
        to_check, _, final, _ = explode(final)
        if to_check:
            continue
        to_check, final = split(final)
        if not to_check:
            break
    return final


def magnitude_of_snail_num(x):
    if isinstance(x, int):
        return x
    return 3 * magnitude_of_snail_num(x[0]) + 2 * magnitude_of_snail_num(x[1])


print(f'Magnitude of final snail after sum: {magnitude_of_snail_num(reduce(sum_snail_nums, snail_nums_list))}')
print(f'Max magnnitude of snail after all the permutations: {max(magnitude_of_snail_num(sum_snail_nums(a, b)) for a, b in permutations(snail_nums_list, 2))}')
