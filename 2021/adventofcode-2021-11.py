with open('input11', 'r') as f:
    lst = []
    for item in f.read().split('\n'):
        lst += [[0] + list(map(int, list(item))) + [0]]
lst.insert(0, [0] * len(lst[0]))
lst.append([0] * len(lst[0]))

steps = 0
total_flash = 0
already_flashing = None


def increase_by_1():
    for i in range(1, len(lst) - 1):
        for j in range(1, len(lst[0]) - 1):
            lst[i][j] += 1


def find_remaining_flashing():
    global already_flashing
    curr_set = set()
    for i in range(1, len(lst) - 1):
        for j in range(1, len(lst[0]) - 1):
            if lst[i][j] > 9 and (i, j) not in already_flashing:
                curr_set.add((i, j))
    return curr_set


def check():
    global already_flashing
    rem_flashing = find_remaining_flashing()
    for i in range(1, len(lst) - 1):
        for j in range(1, len(lst[0]) - 1):
            if lst[i][j] <= 9:
                # Check if neighbour is flashing and increase power of this element
                for x, y in [[i, j + 1], [i + 1, j + 1], [i + 1, j], [i + 1, j - 1], [i, j - 1], [i - 1, j - 1],
                             [i - 1, j], [i - 1, j + 1]]:
                    if (x, y) in rem_flashing:
                        lst[i][j] = lst[i][j] + 1
    already_flashing = rem_flashing.union(already_flashing)
    # New elements with increased power will also start flashing, check again if they are not present in already
    # flashing set
    if rem_flashing:
        check()
    return


def count_flash_make_0():
    global total_flash
    for i in range(1, len(lst) - 1):
        for j in range(1, len(lst[0]) - 1):
            if lst[i][j] >= 10:
                lst[i][j] = 0
                total_flash += 1


while True:
    increase_by_1()
    already_flashing = set()
    check()
    count_flash_make_0()
    steps += 1
    if steps == 100:
        print(f'Total Flash: {total_flash}')
    if all(True if x == 0 else False for y in lst for x in y):
        print(f'STEP where all Flash: {steps}')
        break
