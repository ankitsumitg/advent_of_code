with open('input8', 'r') as f:
    lst = [[x.strip().split('|')[0].strip().split(), x.strip().split('|')[1].strip().split()] for x in f.readlines()]
d = {'a'}
final = 0
for x in lst:
    arr = [0] * 8
    for i in x[0]:
        arr[len(i)] += 1
    # print(arr)
    ans = []
    for i in x[1]:
        if arr[len(i)] == 1:
            ans += [len(i)]
    # print(ans)
    final += len(ans)
print(final)
lst2 = []
for x in lst:
    a = []
    for i in x[0]:
        a += [''.join(sorted(i))]
    a.sort(key=len)
    b = []
    for i in x[1]:
        b += [''.join(sorted(i))]
    lst2 += [[a, b]]
final = 0
for x in lst2:
    d = dict()
    d[x[0][0]] = 1
    d[x[0][1]] = 7
    d[x[0][2]] = 4
    d[x[0][-1]] = 8
    # Finding 2,3,5
    s1 = set(x[0][3])
    s2 = set(x[0][4])
    s3 = set(x[0][5])
    int_all = s1.intersection(s2).intersection(s3)
    # finding 2 and 5
    x1 = (s1 | s2) - int_all
    x2 = (s1 | s3) - int_all
    x3 = (s2 | s3) - int_all
    three = None
    # right now wrong 2 and 5, assumption
    two = None
    five = None
    if len(x1) == 4:
        d[x[0][5]] = 3
        three = x[0][5]
        two = x[0][3]
        five = x[0][4]
    elif len(x2) == 4:
        d[x[0][4]] = 3
        three = x[0][4]
        two = x[0][3]
        five = x[0][5]
    else:
        d[x[0][3]] = 3
        three = x[0][3]
        two = x[0][4]
        five = x[0][5]
    x4 = set(x[0][2]) - int_all - set(three)
    if x4.intersection(two):
        two, five = five, two
    d[two] = 2
    d[five] = 5
    # Finding 0,6,9
    s4 = x[0][-2]
    s5 = x[0][-3]
    s6 = x[0][-4]
    # finding zero
    zero = None
    six = None
    nine = None
    if len(set(s4) | set(five)) > len(s4):
        d[s4] = 0
        six = s5
        nine = s6
    elif len(set(s5) | set(five)) > len(s5):
        d[s5] = 0
        six = s4
        nine = s6
    else:
        d[s6] = 0
        six = s4
        nine = s5
    if len(set(nine) | set(x[0][0])) > len(nine):
        six, nine = nine, six
    d[six] = 6
    d[nine] = 9
    final_num = ''
    for val in x[1]:
        final_num += str(d[val])
    print(final_num)
    final += int(final_num)
print(f'Final Sum: {final}')