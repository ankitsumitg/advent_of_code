from collections import defaultdict

with open('input10', 'r') as f:
    lst = f.read().split('\n')
d = defaultdict(int)
link = {']': '[', '>': '<', ')': '(', '}': '{'}
link_val = {']': 57, '>': 25137, ')': 3, '}': 1197}
link_val_in = {'[': 2, '<': 4, '(': 1, '{': 3}

total_score_lst = []
for s in lst:
    stack = []
    is_incomplete_line = True
    for pair in s:
        if pair in '<{[(':
            stack.append(pair)
        elif stack and stack[-1] == link[pair]:
            stack.pop()
        else:
            d[pair] += 1
            is_incomplete_line = False
            break
    total = 0
    if is_incomplete_line:
        for pair in reversed(stack):
            total *= 5
            total += link_val_in[pair]
        total_score_lst += [total]
total_score_lst.sort()

print(f'Syntax error score: {sum(link_val[i] * d[i] for i in d)}')
print(f'Middle score: {total_score_lst[len(total_score_lst) // 2]}')
