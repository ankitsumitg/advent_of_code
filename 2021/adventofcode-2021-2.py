with open('input2', 'r') as f:
    lst = [x.split() for x in f.read().split('\n')]
d = 0
h = 0
for mov, val in lst:
    if mov == 'forward':
        h += int(val)
    elif mov == 'down':
        d += int(val)
    else:
        d -= int(val)
print(f'Part 1:{d * h}')
d = 0
h = 0
aim = 0
for mov, val in lst:
    if mov == 'forward':
        h += int(val)
        d += aim * int(val)
    elif mov == 'down':
        aim += int(val)
    else:
        aim -= int(val)
print(f'Part 2:{d * h}')
