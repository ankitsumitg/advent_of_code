from collections import defaultdict
from itertools import product

with open('input20') as f:
    rules, g = f.read().split('\n\n')
    G = {(i, j): int(v == '#') for i, l in enumerate(g.split('\n')) for j, v in enumerate(l)}

# relative indices for a position
grid_relative_indices = list(product((-1, 0, 1), repeat=2))


def find_adj_grid(G):
    return {(x + dx, y + dy) for x, y in G for dy, dx in grid_relative_indices}


def solve(g, no_of_gen):
    new_g = None
    for k in range(no_of_gen):
        new_g = defaultdict(bool)
        # grid with border for new elements to be added
        adj_grid = find_adj_grid(g)
        for i, j in adj_grid:
            bin_str = ''
            for dx, dy in grid_relative_indices:
                # infinite plane will only alter in between on or off iff rules[0] == '#' other wise always off
                bin_str += str(g.get((i + dx, j + dy), '01'[k % 2] if rules[0] == '#' else '0'))
            new_g[(i, j)] = int(rules[int(bin_str, 2)] == '#')
        g = new_g
    return new_g


new_G = solve(G, 2)
print(f'Part 1: {sum(new_G.values())}')
new_G = solve(G, 50)
print(f'Part 2: {sum(new_G.values())}')
