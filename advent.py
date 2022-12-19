import sys
 
n = len(sys.argv)
filename = "example"
if n > 1:
    filename = "input"

f = open(filename, "r")

table = dict()
width = 0
height = 0
for line in f.readlines():
    trees = line.split('\n')[0]
    table[height] = trees
    height += 1
    width = max(width, len(trees))

max_scenic_score = 0


def scenic_score_left(table, line, order, current_tree):
    left = 1
    for x in range(0, order):
        if int(table[line][order - 1 - x]) < current_tree:
            left += 1
        else:
            return left
    return left - 1


def scenic_score_right(table, line, order, current_tree):
    right = 1
    for x in range(order + 1, width):
        if int(table[line][x]) < current_tree:
            right += 1
        else:
            return right
    return right - 1


def scenic_score_top(table, line, order, current_tree):
    top = 1
    for x in range(0, line):
        if int(table[line - 1 - x][order]) < current_tree:
            top += 1
        else:
            return top
    return top - 1


def scenic_score_bottom(table, line, order, current_tree):
    bottom = 1
    for x in range(line + 1, height):
        if int(table[x][order]) < current_tree:
            bottom += 1
        else:
            return bottom
    return bottom - 1


def scenic_score(table, line, order):
    current_tree = int(table[line][order])

    left = scenic_score_left(table, line, order, current_tree)
    right = scenic_score_right(table, line, order, current_tree)
    top = scenic_score_top(table, line, order, current_tree)
    bottom = scenic_score_bottom(table, line, order, current_tree)

    score = left * right * top * bottom
    return score


for line in range(1, width - 1):
    for order in range(1, height - 1):
        max_scenic_score = max(max_scenic_score, scenic_score(table, line, order))

print('MAX SCENIC SCORE', max_scenic_score)
