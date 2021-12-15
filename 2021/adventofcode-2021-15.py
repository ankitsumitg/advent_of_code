from queue import PriorityQueue

with open('input15', 'r') as f:
    matrix = [list(map(int, line)) for line in f.read().splitlines()]


# solved using priority queue
def solve_dis(m):
    h, w = len(m), len(m[0])
    pq = PriorityQueue()
    # Add starting position in priority queue
    pq.put((0, (0, 0)))
    visited = {(0, 0), }
    while pq:
        curr_risk, (i, j) = pq.get()
        # Once we reach the end of the matrix, we can stop and return the risk
        if i == h - 1 and j == w - 1:
            return curr_risk
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < h and 0 <= y < w and (x, y) not in visited:
                weight = m[x][y]
                pq.put((curr_risk + weight, (x, y)))
                visited.add((x, y))


def make_big_matrix():
    # Using dict to map weights {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 1}
    d = {i: j % 10 if j % 10 != 0 else 1 for i, j in zip(range(1, 10), range(2, 11))}
    big_matrix = [lst.copy() for lst in matrix]
    for _ in range(4):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                big_matrix[i].append(d[big_matrix[i][j + len(matrix) * _]])
    for _ in range(4):
        for i in range(len(matrix)):
            new_list = list()
            for j in range(len(big_matrix[0])):
                new_list.append(d[big_matrix[i + len(matrix) * _][j]])
            big_matrix.append(new_list)
    return big_matrix


print(f'Part 1 : {solve_dis(matrix)}')
print(f'Part 2 : {solve_dis(make_big_matrix())}')
