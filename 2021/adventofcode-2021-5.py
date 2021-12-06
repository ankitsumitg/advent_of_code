from collections import defaultdict

with open('input5', 'r') as f:
    lst = [[x.split('->')[0].strip().split(','), x.split('->')[1].strip().split(',')] for x in f.read().split('\n')]
d = defaultdict(int)
for i, l in lst:
    x1, y1 = map(int, i)
    x2, y2 = map(int, l)
    if x1 == x2:
        for cor in range(y1 if y1 < y2 else y2, (y1 if y1 > y2 else y2) + 1):
            d[(x1, cor)] += 1
    elif y1 == y2:
        for cor in range(x1 if x1 < x2 else x2, (x1 if x1 > x2 else x2) + 1):
            d[(cor, y1)] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        if x1 < x2 and y1 < y2:
            while x1 <= x2 and y1 <= y2:
                d[(x1, y1)] += 1
                x1 += 1
                y1 += 1
        elif x1 < x2 and y1 > y2:
            while x1 <= x2 and y1 >= y2:
                d[(x1, y1)] += 1
                x1 += 1
                y1 -= 1
        elif x1 > x2 and y1 < y2:
            while x1 >= x2 and y1 <= y2:
                d[(x1, y1)] += 1
                x1 -= 1
                y1 += 1
        else:
            while x1 >= x2 and y1 >= y2:
                d[(x1, y1)] += 1
                x1 -= 1
                y1 -= 1
print(len([x for x in d.values() if x > 1]))
