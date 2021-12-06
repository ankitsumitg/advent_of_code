with open('input1', 'r') as f:
    lst = [int(x) for x in f.read().split('\n')]
print(len([1 for a,b in zip(lst[1:],lst) if a > b]))
lst2 = list()
for i in range(2,len(lst)):
    lst2.append(lst[i] + lst[i-1] + lst[i-2])
print(len([1 for a,b in zip(lst2[1:],lst2) if a > b]))