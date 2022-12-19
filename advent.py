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


nb_visible_trees = 2 * width + 2 * height - 4


def is_visible(table, line, order):
    current_tree = int(table[line][order])

    get_max_left = 0
    for x in range(0, order):
        get_max_left = max(get_max_left, int(table[line][x]))

    if get_max_left < current_tree:
        # Visible from the left
        # print('==> LEFT')
        return True

    get_max_right = 0
    for x in range(order + 1, width):
        get_max_right = max(get_max_right, int(table[line][x]))

    if get_max_right < current_tree:
        # Visible from the right
        # print('==> RIGHT')
        return True

    get_max_top = 0
    for x in range(0, line):
        get_max_top = max(get_max_top, int(table[x][order]))

    if get_max_top < current_tree:
        # Visible from the top
        # print('==> TOP')
        return True

    get_max_bottom = 0
    for x in range(line + 1, height):
        get_max_bottom = max(get_max_bottom, int(table[x][order]))

    if get_max_bottom < current_tree:
        # Visible from the bottom
        # print('==> BOTTOM')
        return True

    return False


for line in range(1, width - 1):
    for order in range(1, height - 1):
        if is_visible(table, line, order):
            nb_visible_trees += 1

print('NB_VISIBLE_TREES', nb_visible_trees)
