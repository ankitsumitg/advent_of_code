from collections import defaultdict

STEPS = 40
d = defaultdict(int)
joiners = defaultdict(int)

with open('input14', 'r') as f:
    s, waste, *conn = f.read().splitlines()
    conn = dict(r.split(' -> ') for r in conn)
    for i, j in zip(s, s[1:]):
        joiners[i + j] += 1
    for k in s:
        d[k] += 1
for _ in range(STEPS):
    for key, val in joiners.copy().items():
        link = conn[key]
        joiners[key] -= val
        joiners[key[0] + link] += val
        joiners[link + key[1]] += val
        d[link] += val
    print(f'Step {_ + 1}: {max(d.values()) - min(d.values())}')
