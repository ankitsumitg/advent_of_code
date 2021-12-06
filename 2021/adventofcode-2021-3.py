with open('input3', 'r') as f:
    lst = f.read().split('\n')
    lst2 = list(lst)
gamma = ''
epi = ''
for i in range(len(lst[0])):
    one = [x[i] for x in lst].count('1')
    zero = len(lst) - one
    epi += '1' if one > zero else '0'
    gamma += '1' if one < zero else '0'
print(int(epi, 2) * int(gamma, 2)) #4138664

#2nd question
for i in range(len(lst[0])):
    one = [x[i] for x in lst].count('1')
    zero = len(lst) - one
    keep ='1' if one >= zero else '0'
    if len(lst) == 1:
        break
    lst = [x for x in lst if x[i] == keep]
a = int(lst[0],2)
for i in range(len(lst2[0])):
    one = [x[i] for x in lst2].count('1')
    zero = len(lst2) - one
    keep ='1' if one < zero else '0'
    if len(lst2) == 1:
        break
    lst2 = [x for x in lst2 if x[i] == keep]
b = int(lst2[0],2)
print(a*b)