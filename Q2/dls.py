
grid = [
    ['#', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '#', '.', '.'],
    ['#', '.', '.', 'B', '.', '.'],
    ['#', '.', '#', '#', '.', '.'],
    ['#', '.', '#', '.', '.', '.'],
    ['A', '#', '#', '.', '.', '.'],

]






def is_valid(r, c, grid, visited):
    rows = len(grid)
    cols = len(grid[0])

    if r < 0 or r >= rows or c < 0 or c >= cols: #out of bounds
        return False

    if grid[r][c] == '.':          # '.' means gray/blocked (change if needed)
        return False

    if (r, c) in visited:          # already visited 
        return False

    return True


def dls(row, col, limit):
    stack = []
    visited = set()
    depth = 0
    

    if not is_valid(row, col, grid, visited):    # start
        return False

    stack.append((row, col))
    visited.add((row, col))

    while stack:
        row, col = stack.pop()
        print(f"go to ({row}, {col})")

        if grid[row][col] == 'B':         # goal check
            print("we have reached B")
            return True
        
        if depth == limit:
            depth = 0
            continue

        for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:         # 3) explore neighbors (level by level)

            newRow = row + dr
            newCol = col + dc

            if is_valid(newRow, newCol, grid, visited):
                visited.add((newRow, newCol))
                stack.append((newRow, newCol))
                depth += 1
    print("couldn't reach B with the limit")
    return False        # nothing found




print("dls algorithm with limit 4")
dls(6,0,4)


print("dls algorithm with limit 8")
dls(6,0,8)