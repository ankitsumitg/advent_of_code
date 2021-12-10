with open('input10', 'r') as f:
    lst = f.read().split('\n')

link = {']': '[', '>': '<', ')': '(', '}': '{'}
pair_val = {']': 57, '>': 25137, ')': 3, '}': 1197, '[': 2, '<': 4, '(': 1, '{': 3}

syntax_error_score = 0
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
            syntax_error_score += pair_val[pair]
            is_incomplete_line = False
            break
    total = 0
    if is_incomplete_line:
        while stack:
            total = total * 5 + pair_val[stack.pop()]
        total_score_lst += [total]
total_score_lst.sort()

print(f'Syntax error score: {syntax_error_score}')
print(f'Middle score: {total_score_lst[len(total_score_lst) // 2]}')
