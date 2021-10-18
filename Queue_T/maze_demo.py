maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x, y-1),
    lambda x, y: (x+1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x-1, y)
]

def maze_search(x1, y1, x2, y2):
    stack = []

    stack.append((x1, y1))
    maze[x1][y1] = 2
    while(len(stack) > 0):
        cur_node = stack[-1]
        if cur_node[0] == x2 and cur_node[1] == y2:
            print("the path was found")
            for i in stack:
                print(i)
            break
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2  # to make sure that The path taken will not be retraced
                break
        else:
            stack.pop()
    else:
        print("there is no path to the goal point.")

maze_search(1, 1, 8, 8)
