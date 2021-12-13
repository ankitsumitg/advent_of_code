index = []
fold = []
x_max = 0
y_max = 0
with open('input13', 'r') as f:
    for item in f.read().splitlines():
        if not item.startswith('fold along') and item:
            j, i = map(int, item.split(','))
            index.append([j, i])
            if j > x_max:
                x_max = j
            if i > y_max:
                y_max = i
        elif item:
            fold.append([item.split('=')[0][-1], int(item.split('=')[-1])])

# initialize grid with zeroes
grid = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]
# fill grid with 1 where dot is present
for j, i in index:
    grid[i][j] = 1
# reverse the fold list
fold.reverse()

# to keep track of last x, y fold crease
initial_y = len(grid)
initial_x = len(grid[0])
times_folded = 0

while fold:
    key, val = fold.pop()
    initial = 1
    times_folded += 1
    if key == 'y':  # For horizontal fold
        initial = val - 1
        for i in range(val + 1, initial_y):
            for j in range(initial_x):
                if initial >= 0:
                    # Using bitwise_OR to make the value of mirror part
                    grid[initial][j] |= grid[i][j]
            initial -= 1
        initial_y = val
        print(
            f'Total dots after {times_folded} fold: {sum(1 for i in grid[:initial_y] for j in i[:initial_x] if j == 1)}')
    else:  # For vertical fold
        for i in range(initial_y):
            initial = val - 1
            for j in range(val + 1, initial_x):
                if j - initial >= 0:
                    grid[i][initial] |= grid[i][j]
                    initial -= 1
        initial_x = val
        print(
            f'Total dots after {times_folded} fold: {sum(1 for i in grid[:initial_y] for j in i[:initial_x] if j == 1)}')

print('Final code')
for i in grid[:initial_y]:
    for j in i[:initial_x]:
        print('#' if j == 1 else '.', end='')
    print()
