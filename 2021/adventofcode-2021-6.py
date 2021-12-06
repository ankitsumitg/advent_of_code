DAYS = 256
with open('input6','r') as f:
    lst = list(map(int,f.read().strip().split(',')))
arr = [0] * 9
for fish in lst:
    arr[fish] += 1
for _ in range(DAYS):
    start = arr[0]
    for j in range(0,8,):
        arr[j] = arr[j+1]
    arr[6] += start
    arr[8] = start
assert 1686252324092 == sum(arr), 'Not Equal'

