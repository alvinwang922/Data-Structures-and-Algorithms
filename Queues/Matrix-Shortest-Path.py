"""
Find length of shortest path in a matrix from top left corner 
to bottom right corner.
1s - walls
0s - empty spaces; can travel
"""


def shortest_path(matrix):
    queue = []
    queue.append([0, 0, 1])
    matrix[0][0] = 1
    while queue:
        x, y, distance = queue.pop(0)
        print(x, y, distance)
        if x == len(matrix[0]) - 1 and y == len(matrix) - 1:
            return distance
        right = [x + 1, y, distance + 1]
        left = [x - 1, y, distance + 1]
        down = [x, y + 1, distance + 1]
        up = [x, y - 1, distance + 1]
        if isValid(matrix, right):
            queue.append(right)
            matrix[right[1]][right[0]] = 1
        if isValid(matrix, left):
            queue.append(left)
            matrix[left[1]][left[0]] = 1
        if isValid(matrix, down):
            queue.append(down)
            matrix[down[1]][down[0]] = 1
        if isValid(matrix, up):
            queue.append(up)
            matrix[up[1]][up[0]] = 1
    return -1


def isValid(matrix, direction):
    x, y, distance = direction
    if x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix):
        return False
    if matrix[y][x] == 1:
        return False
    return True


print(shortest_path([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0],
                     [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]]))
print(shortest_path([[0, 0], [1, 0]]))
print("The values above should be 8 and 3.")
