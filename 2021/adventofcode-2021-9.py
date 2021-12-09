import math

with open('input9', 'r') as f:
    lst = []
    for x in f.read().split('\n'):
        lst += [[10] + list(map(int, [i for i in x])) + [10]]
# Construct wall of 10 around the block
lst.insert(0, [10] * len(lst[0]))
lst.append([10] * len(lst[0]))

risk_level = 0
basin = []
vis = [[False] * len(lst[0]) for _ in range(len(lst))]


def find_basin(x, y):
    if lst[x][y] >= 9 or vis[x][y]:
        return 0
    ans = 1
    vis[x][y] = True
    ans += find_basin(x, y + 1)
    ans += find_basin(x + 1, y)
    ans += find_basin(x, y - 1)
    ans += find_basin(x - 1, y)
    return ans


for i in range(1, len(lst) - 1):
    for j in range(1, len(lst[0]) - 1):
        v = lst[i][j]
        if v < lst[i][j + 1] and v < lst[i + 1][j] and v < lst[i][j - 1] and v < lst[i - 1][j]:
            risk_level += v + 1
            basin += [find_basin(i, j)]

print(f'Risk Level: {risk_level}')
basin.sort(reverse=True)
print(f'3 largest basins product: {math.prod(basin[:3])}')
