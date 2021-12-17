from re import findall

s = 'target area: x=156..202, y=-110..-69'
x1, x2, y1, y2 = map(int, findall('-?\\d+', s))


# what ever y coordinates we hit while going up, we will hit these coordinates again
# that means, we will reach again at 0. So At 0 vy will be -initial_vy
# and the next point we will hit will be at initial_vy + 1 (On negative direction)
# this vy should be equal to our lower bound of y
# initial_vy + 1 == abs(y1), initial_vy = abs(y1) - 1
def is_correct_initial_velocity(vx, vy, pos_x=0, pos_y=0):
    # overshoot/undershoot condition, return
    if pos_x > x2 or pos_y < y1: return False
    # we are inside the box
    if x1 <= pos_x <= x2 and y1 <= pos_y <= y2: return True
    return is_correct_initial_velocity(vx - int(vx > 0), vy - 1, pos_x + vx, pos_y + vy)


initial_vy = abs(y1) - 1
# Brute force the correct points
initial_velocity_list = [is_correct_initial_velocity(x, y) for x in range(-x2, 1 + x2) for y in range(y1, -y1)]
print(f'hMax: {initial_vy * (initial_vy + 1) // 2}')
print(f'Total Initial velocity: {initial_velocity_list.count(True)}')
