import statistics
with open('input7','r') as f:
    lst = list(map(int,f.read().strip().split(',')))
mediann = statistics.median(lst)
print(int(sum(abs(x-mediann) for x in lst)))
meann = int(statistics.mean(lst))
print(int(sum(abs(x-meann)*(abs(x-meann) + 1)/2 for x in lst)))