with open('input4', 'r') as f:
    lst = f.read().split('\n')
num = lst[0].split(',')
i = 2
d = dict()
b = 0
while i < len(lst):
    l = list()
    for j in range(5):
        l.append(lst[i + j].split())
    d[b] = l
    i += 6
    b += 1


def check(lst):
    for x in lst:
        if all('*' in i for i in x):
            return True
    for x in zip(*lst):
        if all('*' in i for i in x):
            return True
    return False


def replace(lst, val):
    ans = [[el + '*' if el == val else el for el in ll] for ll in lst]
    return ans


for n in num:
    for i in range(b):
        if i in d:
            d[i] = replace(d[i], n)
            if check(d[i]):
                s = 0
                for cc in d[i]:
                    for nn in cc:
                        s += 0 if '*' in nn else int(nn)
                print(f'Board {i + 1}: {s * int(n)}')
                if len(d) > 1:
                    d.pop(i)
                else:
                    exit()
