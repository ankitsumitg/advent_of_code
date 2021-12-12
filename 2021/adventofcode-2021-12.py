from collections import defaultdict

with open('input12', 'r') as f:
    links = defaultdict(list)
    for link in f.read().split('\n'):
        node1, node2 = link.split('-')
        links[node1].append(node2)
        links[node2].append(node1)

start = 'start'
end = 'end'


def count(start_here, max_time_to_visit, visited):
    global links, total
    if start_here == end:
        total += 1
        return
    if start_here in visited:
        if start_here == start:
            return
        if start_here.islower():
            if max_time_to_visit == 1:
                return
            max_time_to_visit -= 1
    for node in links[start_here]:
        count(node, max_time_to_visit, visited | {start_here})


total = 0
count(start, 1, set())
print(f'Total Ways (Can visit only once): {total}')
total = 0
count(start, 2, set())
print(f'Total Ways (Can visit only twice): {total}')
